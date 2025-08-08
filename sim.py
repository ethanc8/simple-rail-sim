#!/usr/bin/env python3
import simlib
import importlib
import sys

# user interface

scenario_id = sys.argv[1]
scenario = importlib.import_module(f'scenarios.{scenario_id}')
print(f"Scenario: {scenario.scenario_name}")

vehicle_id = sys.argv[2]
vehicle = importlib.import_module(f'vehicles.{vehicle_id}')
print(f"Vehicle: {vehicle.name}")

# ---- 2) Set train & track parameters ----

actions_df, timetable_df = simlib.simulate(scenario, vehicle)
# Stringline diagram
fig = simlib.plot_stringline(actions_df, timetable_df)
outpath = 'out/stringline.png'
fig.savefig(outpath)
print(f"Stringline diagram saved to {outpath}")
