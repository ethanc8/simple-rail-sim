#!/usr/bin/env python3
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

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

# Other utility

def timestamp_to_str(timestamp):
    hh, rem = divmod(timestamp, 3600)
    mm, ss  = divmod(rem, 60)
    return f"{int(hh):02d}:{int(mm):02d}:{int(ss):02d}"

def timestamp_to_str_nosec(timestamp):
    hh, rem = divmod(timestamp, 3600)
    mm, ss  = divmod(rem, 60)
    return f"{int(hh):02d}:{int(mm):02d}"

# ---- 2) Set train & track parameters ----

def simulate(scenario, vehicle, depart_time=0.0):
    route = scenario.route
    stops = scenario.stops

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

    timetable = []
    actions = []
    t_cum = depart_time # seconds since departure
    v_prev = 0.0 # m/s
    pos_cum = 0.0 # m

    # Departure
    timetable.append({
        'Station': stops[0.0],
        'MP': 0.0,
        'Arrival': None,
        'Departure': timestamp_to_str(depart_time)
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
                'End Time': timestamp_to_str(t_cum + t1),
                'Start Time (s)': (t_cum),
                'End Time (s)': (t_cum + t1)
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
                'End Time': timestamp_to_str(t_cum + t2),
                'Start Time (s)': (t_cum),
                'End Time (s)': (t_cum + t2)
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
                'End Time': timestamp_to_str(t_cum + t3),
                'Start Time (s)': (t_cum),
                'End Time (s)': (t_cum + t3)
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
                'End Time': timestamp_to_str(t_cum + scenario.dwell_time),
                'Start Time (s)': (t_cum),
                'End Time (s)': (t_cum + scenario.dwell_time)
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

    return actions_df, timetable_df

def plot_stringline(actions_df, timetable_df, color='tab:blue', linewidth=1):
    """
    Draws a stringline diagram (position vs time) with:
      - one uniform color
      - accel/decel as smooth quadratic curves
      - cruise/dwell as straight lines
    """
    # map station names → vertical positions (m)
    mile2m = 1609.34
    station_positions = {
        row['Station']: row['MP'] * mile2m
        for _, row in timetable_df.iterrows() if row['MP'] is not None
    }
    
    fig, ax = plt.subplots(figsize=(10,6))
    
    for _, row in actions_df.iterrows():
        t0, t1 = row['Start Time (s)'], row['End Time (s)']
        x0, x1 = row['Start Pos (m)'], row['End Pos (m)']
        phase = row['Phase']
        
        if phase in ('Accelerate','Decelerate'):
            # TODO: draw a correct curve rather than quadratic
            # draw a quadratic curve between endpoints
            ts = np.linspace(t0, t1, 50)
            s = (ts - t0) / (t1 - t0)              # normalized [0→1]
            # ease-in-out: accel → s^2 ; decel → 1 - (1-s)^2
            if phase == 'Accelerate':
                weights = s**2
            else:
                weights = 1 - (1 - s)**2
            xs = x0 + weights * (x1 - x0)
            ax.plot(ts, xs, color=color, linewidth=linewidth)
        
        else:
            # straight line for Cruise or Dwell
            ax.plot([t0, t1], [x0, x1], color=color, linewidth=linewidth)
    
    # annotate stations on the y-axis
    ax.set_yticks(list(station_positions.values()))
    ax.set_yticklabels(list(station_positions.keys()))
    
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: timestamp_to_str(x)))
    ax.set_xlabel('Time')
    ax.set_ylabel('Station')
    ax.set_title('Stringline Diagram')
    ax.grid(True)
    plt.tight_layout()
    
    return fig

def _hhmmss_to_sec(s):
    h, m, sec = map(int, str(s).split(':'))
    return h*3600 + m*60 + sec

def _get_numeric(row, key_num, key_str, is_time=False):
    """Return numeric value from either a numeric column or HH:MM:SS string."""
    if key_num in row and row[key_num] is not None and row[key_num] == row[key_num]:
        return float(row[key_num])
    if key_str in row and row[key_str] is not None and row[key_str] == row[key_str]:
        return float(_hhmmss_to_sec(row[key_str])) if is_time else float(row[key_str])
    raise KeyError(f"Neither '{key_num}' nor '{key_str}' found/usable in row.")

def plot_stringline_multi(
    scenarios,                      # list of (actions_df, timetable_df, label, color)
    minutes=True,                    # x-axis in minutes
    linewidth=1,
):
    """
    Plot multiple scenarios on a single stringline (time-distance) diagram.

    Each timetable_df should have 'Station' and 'MP' (milepost) rows for y-axis labels.
    """

    # Collect station y-axis ticks from all scenarios (union of stations)
    mile2m = 1609.34
    station_pos = {}
    for _actions_df, ttab, _label, _color in scenarios:
        for _, r in ttab.iterrows():
            if 'MP' in r and r['MP'] is not None and r['MP'] == r['MP']:
                station_pos[r['Station']] = float(r['MP']) * mile2m

    # Stable order (by position increasing)
    station_items = sorted(station_pos.items(), key=lambda kv: kv[1])

    fig, ax = plt.subplots(figsize=(11, 7))

    # Plot each scenario
    for actions_df, _ttab, label, color in scenarios:
        first_segment = True
        for _, row in actions_df.iterrows():
            t0, t1 = row['Start Time (s)'], row['End Time (s)']
            x0, x1 = row['Start Pos (m)'], row['End Pos (m)']
            phase = row['Phase']

            if phase in ('Accelerate', 'Decelerate'):
                # TODO: draw a correct curve rather than quadratic
                # simple quadratic curve between endpoints
                if t1 == t0:
                    continue
                ts = np.linspace(t0, t1, 60)
                s = (ts - t0) / (t1 - t0)
                if phase == 'Accelerate':
                    w = s**2
                else:
                    w = 1 - (1 - s)**2
                xs = x0 + w * (x1 - x0)
                ax.plot(ts, xs, color=color, linewidth=linewidth, label=label if first_segment else None)
            else:
                ax.plot([t0, t1], [x0, x1], color=color, linewidth=linewidth, label=label if first_segment else None)

            first_segment = False

    # Y-axis: station names at their mileposts
    if station_items:
        y_vals = [p for _, p in station_items]
        y_labs = [s for s, _ in station_items]
        ax.set_yticks(y_vals)
        ax.set_yticklabels(y_labs)

    # X-axis label/format
    ax.set_xlabel('Time (minutes)' if minutes else 'Time (seconds)')
    if minutes:
        ax.xaxis.set_major_locator(MultipleLocator(15 * 60))
        ax.xaxis.set_minor_locator(MultipleLocator(5 * 60))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: timestamp_to_str_nosec(x)))

    ax.set_ylabel('Station')
    ax.set_title('Stringline Diagram')
    ax.grid(True, which='both', linestyle=':', linewidth=0.7)
    ax.legend(loc='best', frameon=True)

    fig.tight_layout()
    return fig
