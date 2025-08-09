#!/usr/bin/env python3
import simlib
import importlib
import sys

multitrip_id = sys.argv[1]
multitrip = importlib.import_module(f'multitrips.{multitrip_id}')

solved_trips = []

for trip in multitrip.trips:
    scenario_id, vehicle_id, depart_time, label, color = trip
    scenario = importlib.import_module(f'scenarios.{scenario_id}')
    print(f"Scenario: {scenario.scenario_name}")

    vehicle = importlib.import_module(f'vehicles.{vehicle_id}')
    print(f"Vehicle: {vehicle.name}")

    # ---- 2) Set train & track parameters ----

    actions_df, timetable_df = simlib.simulate(scenario, vehicle, depart_time)
    solved_trips.append((actions_df, timetable_df, label, color))

# Stringline diagram
fig = simlib.plot_stringline_multi(solved_trips, name=multitrip.name)
outpath = 'out/stringline.png'
fig.savefig(outpath)
print(f"Stringline diagram saved to {outpath}")
