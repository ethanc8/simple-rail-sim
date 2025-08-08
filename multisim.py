#!/usr/bin/env python3
import simlib
import importlib
import sys

# # UP-N, locals every 15 min, expresses every 30 min, 7.5 min offset between locals + expresses
# trips = [
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 0, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 7.5 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 15 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 30 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 37.5 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 45 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 60 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 67.5 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 75 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 90 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 97.5 * 60, 'Express', 'tab:green'),
# ]

# # UP-N, locals every 15 min, expresses every 30 min, cross-platform transfer at Evanston Davis
# trips = [
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 0, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 5 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 15 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 30 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 35 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 45 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 60 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 65 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 75 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 90 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 95 * 60, 'Express', 'tab:green'),
# ]

# # UP-N, locals every 15 min, expresses every 30 min, cross-platform transfer at Winnetka
# trips = [
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 0, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 10 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 15 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 30 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 40 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 45 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 60 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 70 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 75 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 90 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 100 * 60, 'Express', 'tab:green'),
# ]

# # UP-N, locals every 15 min, expresses every 30 min, cross-platform transfer at Highland Park
# trips = [
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 0, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 14 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 15 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 30 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 44 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 45 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 60 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 74 * 60, 'Express', 'tab:green'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 75 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 90 * 60, 'Local', 'tab:red'),
#     ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 104 * 60, 'Express', 'tab:green'),
# ]

# UP-N, locals every 15 min, expresses every 30 min, cross-platform transfer at Lake Forest
trips = [
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 0, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 1.5 * 60, 'Express', 'tab:green'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 15 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 30 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 31.5 * 60, 'Express', 'tab:green'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 45 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 60 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 61.5 * 60, 'Express', 'tab:green'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 75 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.local__90mph', 'stadler_flirt', 90 * 60, 'Local', 'tab:red'),
    ('metra.upn.krm_highlevel.limited__90mph', 'stadler_flirt', 91.5 * 60, 'Express', 'tab:green'),
]


solved_trips = []

for trip in trips:
    scenario_id, vehicle_id, depart_time, label, color = trip
    scenario = importlib.import_module(f'scenarios.{scenario_id}')
    print(f"Scenario: {scenario.scenario_name}")

    vehicle = importlib.import_module(f'vehicles.{vehicle_id}')
    print(f"Vehicle: {vehicle.name}")

    # ---- 2) Set train & track parameters ----

    actions_df, timetable_df = simlib.simulate(scenario, vehicle, depart_time)
    solved_trips.append((actions_df, timetable_df, label, color))

# Stringline diagram
fig = simlib.plot_stringline_multi(solved_trips)
outpath = 'out/stringline.png'
fig.savefig(outpath)
print(f"Stringline diagram saved to {outpath}")
