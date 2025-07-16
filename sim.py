#!/usr/bin/env python3
"""
Train Performance Simulation: Chicago → Champaign (Integral Method)

This script uses a speed-domain integral approach to compute:
  1) A station-to-station timetable (with 1-min dwell at Kankakee)
  2) A breakdown of when/where the train is accelerating, cruising, or decelerating.

Requirements:
  • Python 3.7+
  • numpy, pandas
"""

import numpy as np
import pandas as pd

# ---- 1) Define the integral-based accel/decel functions ----

def integratel(f, x1, x2, n=2000):
    """Numerical integral of f(x) from x1 to x2 using the trapezoid rule."""
    xs = np.linspace(x1, x2, n)
    ys = f(xs)
    return np.trapezoid(ys, xs)

def make_acctime_fn(k, a, b, c, m0):
    """Return a function t_acc(x1→x2) in seconds."""
    def fn(x1, x2):
        if x2 <= x1: return 0.0
        accel = lambda x: np.maximum(x / (k - a*x - b*x**2 - c*x**3), 1/m0)
        return integratel(accel, x1, x2)
    return fn

def make_accdist_fn(k, a, b, c, m0):
    """Return a function d_acc(x1→x2) in meters."""
    def fn(x1, x2):
        if x2 <= x1: return 0.0
        distf = lambda x: np.maximum(x**2 / (k - a*x - b*x**2 - c*x**3), x/m0)
        return integratel(distf, x1, x2)
    return fn

def make_dectime_fn(k, a, b, c, m0):
    """Return a function t_dec(x1→x2) in seconds."""
    def fn(x1, x2):
        if x1 <= x2: return 0.0
        decel = lambda x: np.maximum(x / (k + a*x + b*x**2 + c*x**3), 1/m0)
        return integratel(decel, x2, x1)
    return fn

def make_decdist_fn(k, a, b, c, m0):
    """Return a function d_dec(x1→x2) in meters."""
    def fn(x1, x2):
        if x1 <= x2: return 0.0
        distf = lambda x: np.maximum(x**2 / (k + a*x + b*x**2 + c*x**3), x/m0)
        return integratel(distf, x2, x1)
    return fn


# ---- 2) Set train & track parameters ----

power_weight_ratio      = 26.74          # kW per tonne → power/weight ratio
a_coef = 0.0059         # Davis resistance a
b_coef = 0.000118       # Davis resistance b
c_coef = 0.000018       # Davis resistance c
initial_accel     = 0.9            # initial max accel (m/s²)
mile2m = 1609.34

# Create the advance functions:
t_acc = make_acctime_fn(power_weight_ratio, a_coef, b_coef, c_coef, initial_accel)
d_acc = make_accdist_fn(power_weight_ratio, a_coef, b_coef, c_coef, initial_accel)
t_dec = make_dectime_fn(power_weight_ratio, a_coef, b_coef, c_coef, initial_accel)
d_dec = make_decdist_fn(power_weight_ratio, a_coef, b_coef, c_coef, initial_accel)


# ---- 3) Define the route segments ----

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)
route = [
    (  0.0,   3.0, 100, False),
    (  3.0,   4.2, 150, False),
    (  4.2,   7.0, 250, False),
    (  7.0,  16.5, 300, False),
    ( 16.5,  17.0, 250, False),
    ( 17.0,  47.9, 300, False),
    ( 47.9,  48.4, 280, False),
    ( 48.4,  53.7, 300, False),
    ( 53.7,  55.9, 150, True ),  # Kankakee stop
    ( 55.9,  57.0, 150, False),
    ( 57.0,  64.0, 300, False),
    ( 64.0, 127.8, 177, True ),  # Champaign stop
]

stops = {
    0.0: 'Chicago Union Station',
    55.9: 'Kankakee',
    127.8: 'Champaign'
}

# Helper to convert speeds:
kmh2ms = lambda v: v * 1000/3600
ms2kmh = lambda v: v * 3600/1000


# ---- 4) Build the station timetable ----

def timestamp_to_str(timestamp):
    hh, rem = divmod(timestamp, 3600)
    mm, ss  = divmod(rem, 60)
    return f"{int(hh):02d}:{int(mm):02d}:{int(ss):02d}"

timetable = []
actions = []
t_cum = 0.0  # seconds since departure
v_prev = 0.0 # m/s
pos_cum = 0.0 # m

# Departure from Chicago
timetable.append({
    'Station': stops[0.0],
    'MP': 0.0,
    'Arrival': None,
    'Departure': '00:00:00'
})

for start, end, spd, stop in route:
    segment_start_pos = pos_cum
    segment_length = (end - start) * mile2m
    v_lim   = kmh2ms(spd)
    # determine next speed for decel
    v_next = 0.0 if stop else kmh2ms(route[route.index((start,end,spd,stop))+1][2])

    # 1) Acceleration block
    if v_prev < v_lim:
        t1 = t_acc(v_prev, v_lim)
        d1 = d_acc(v_prev, v_lim)
        actions.append({
            'Phase': 'Accelerate',
            'Start Pos (m)': segment_start_pos,
            'End Pos (m)'  : segment_start_pos + d1,
            'Start Speed (km/h)': ms2kmh(v_prev),
            'End Speed (km/h)': ms2kmh(v_lim),
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + t1)
        })
        t_cum += t1
        pos_cum += d1

    # 2) Cruise block
    d3 = d_dec(v_lim, v_next)
    d2 = segment_length - (pos_cum - segment_start_pos) - d3
    if d2 > 0:
        t2 = d2 / v_lim
        actions.append({
            'Phase': 'Cruise',
            'Start Pos (m)': pos_cum,
            'End Pos (m)'  : pos_cum + d2,
            'Start Speed (km/h)': ms2kmh(v_lim),
            'End Speed (km/h)': ms2kmh(v_lim),
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + t2)
        })
        t_cum += t2
        pos_cum += d2

    # 3) Deceleration block
    if v_next < v_lim:
        t3 = t_dec(v_lim, v_next)
        d3 = d_dec(v_lim, v_next)
        actions.append({
            'Phase': 'Decelerate',
            'Start Pos (m)': pos_cum,
            'End Pos (m)'  : pos_cum + d3,
            'Start Speed (km/h)': ms2kmh(v_lim),
            'End Speed (km/h)': ms2kmh(v_next),
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + t3)
        })
        t_cum += t3
        pos_cum += d3

    # 4) Dwell (if stop)
    if stop:
        actions.append({
            'Phase': 'Dwell',
            'Start Pos (m)': pos_cum,
            'End Pos (m)'  : pos_cum,
            'Start Speed (km/h)': 0.0,
            'End Speed (km/h)': 0.0,
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + 60.0)
        })

        timetable.append({
            'Station': stops[end],
            'MP'     : end,
            'Arrival': timestamp_to_str(t_cum),
            'Departure': timestamp_to_str(t_cum + 60.0)
        })

        t_cum += 60.0

        v_prev = 0.0
    else:
        v_prev = v_lim

timetable_df = pd.DataFrame(timetable)
print("\n=== Timetable ===")
print(timetable_df.to_string(index=False))

actions_df = pd.DataFrame(actions)
print("\n=== Action Breakdown ===")
print(actions_df[['Phase','Start Pos (m)','End Pos (m)','Start Speed (km/h)', 'End Speed (km/h)', 'Start Time','End Time']].to_string(index=False))
