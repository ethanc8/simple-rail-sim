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
import importlib
import sys

# user interface

scenario_id = sys.argv[1]
scenario = importlib.import_module(f'scenarios.{scenario_id}')
print(f"Scenario: {scenario.scenario_name}")
route = scenario.route
stops = scenario.stops

vehicle_id = sys.argv[2]
vehicle = importlib.import_module(f'vehicles.{vehicle_id}')
print(f"Vehicle: {vehicle.name}")


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

# Create the advance functions:
t_acc = make_acctime_fn(vehicle.power_weight_ratio, vehicle.a_coef, vehicle.b_coef, vehicle.c_coef, vehicle.initial_accel)
d_acc = make_accdist_fn(vehicle.power_weight_ratio, vehicle.a_coef, vehicle.b_coef, vehicle.c_coef, vehicle.initial_accel)
t_dec = make_dectime_fn(vehicle.power_weight_ratio, vehicle.a_coef, vehicle.b_coef, vehicle.c_coef, vehicle.initial_accel)
d_dec = make_decdist_fn(vehicle.power_weight_ratio, vehicle.a_coef, vehicle.b_coef, vehicle.c_coef, vehicle.initial_accel)

# Helper to convert speeds:
kmh2ms = lambda v: v * 1000/3600
ms2kmh = lambda v: v * 3600/1000
mile2m = 1609.34

vehicle_max_speed_ms = kmh2ms(vehicle.max_speed)

def limited_kmh2ms(v):
    return min(kmh2ms(v), vehicle_max_speed_ms)

# ---- 3) Build the station timetable ----

def timestamp_to_str(timestamp):
    hh, rem = divmod(timestamp, 3600)
    mm, ss  = divmod(rem, 60)
    return f"{int(hh):02d}:{int(mm):02d}:{int(ss):02d}"

timetable = []
actions = []
t_cum = 0.0  # seconds since departure
v_prev = 0.0 # m/s
pos_cum = 0.0 # m

# Departure
timetable.append({
    'Station': stops[0.0],
    'MP': 0.0,
    'Arrival': None,
    'Departure': '00:00:00'
})

def solve_peak(v0, v1, v2, length):
    """Find peak speed v_peak <= v1 if no cruise possible."""
    lo, hi = v0, v1
    for _ in range(30):
        mid = 0.5*(lo+hi)
        if d_acc(v0,mid)+d_dec(mid,v2) > length: hi = mid
        else: lo = mid
    return lo

for start, end, spd, stop in route:
    segment_start_pos = pos_cum
    segment_length = (end - start) * mile2m
    v_lim   = limited_kmh2ms(spd)
    cruising = True
    # determine next speed for decel
    v_next = 0.0 if stop else limited_kmh2ms(route[route.index((start,end,spd,stop))+1][2])

    # check reachability
    if d_acc(v_prev, v_lim) + d_dec(v_lim, v_next) > segment_length:
        # adjust peak
        v_max = solve_peak(v_prev, v_lim, v_next, segment_length)
        cruising = False
    else:
        v_max = v_lim

    # 1) Acceleration block
    if v_prev < v_max:
        t1 = t_acc(v_prev, v_max)
        d1 = d_acc(v_prev, v_max)
        actions.append({
            'Phase': 'Accelerate',
            'Start Pos (m)': segment_start_pos,
            'End Pos (m)'  : segment_start_pos + d1,
            'Start Pos (mi)': segment_start_pos / mile2m,
            'End Pos (mi)'  : (segment_start_pos + d1) / mile2m,
            'Start Speed (km/h)': ms2kmh(v_prev),
            'End Speed (km/h)': ms2kmh(v_max),
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + t1)
        })
        t_cum += t1
        pos_cum += d1

    # 2) Cruise block
    d3 = d_dec(v_max, v_next)
    d2 = segment_length - (pos_cum - segment_start_pos) - d3
    if d2 > 0:
        t2 = d2 / v_max
        if cruising:
            actions.append({
                'Phase': 'Cruise',
                'Start Pos (m)': pos_cum,
                'End Pos (m)'  : pos_cum + d2,
                'Start Pos (mi)': pos_cum / mile2m,
                'End Pos (mi)'  : (pos_cum + d2) / mile2m,
                'Start Speed (km/h)': ms2kmh(v_max),
                'End Speed (km/h)': ms2kmh(v_max),
                'Start Time': timestamp_to_str(t_cum),
                'End Time': timestamp_to_str(t_cum + t2)
            })
        t_cum += t2
        pos_cum += d2

    # 3) Deceleration block
    if v_next < v_max:
        t3 = t_dec(v_max, v_next)
        d3 = d_dec(v_max, v_next)
        actions.append({
            'Phase': 'Decelerate',
            'Start Pos (m)': pos_cum,
            'End Pos (m)'  : pos_cum + d3,
            'Start Pos (mi)': pos_cum / mile2m,
            'End Pos (mi)'  : (pos_cum + d3) / mile2m,
            'Start Speed (km/h)': ms2kmh(v_max),
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
            'Start Pos (mi)': pos_cum / mile2m,
            'End Pos (mi)'  : pos_cum / mile2m,
            'Start Speed (km/h)': 0.0,
            'End Speed (km/h)': 0.0,
            'Start Time': timestamp_to_str(t_cum),
            'End Time': timestamp_to_str(t_cum + scenario.dwell_time)
        })

        timetable.append({
            'Station': stops[end],
            'MP'     : end,
            'Arrival': timestamp_to_str(t_cum),
            'Departure': timestamp_to_str(t_cum + scenario.dwell_time)
        })

        t_cum += scenario.dwell_time

        v_prev = 0.0
    else:
        v_prev = v_max

actions_df = pd.DataFrame(actions)
print("\n=== Action Breakdown ===")
print(actions_df[['Phase','Start Pos (m)','End Pos (m)','Start Pos (mi)','End Pos (mi)','Start Speed (km/h)', 'End Speed (km/h)', 'Start Time','End Time']].to_string(index=False))

timetable_df = pd.DataFrame(timetable)
print("\n=== Timetable ===")
print(timetable_df.to_string(index=False))
