#!/usr/bin/env python3
"""
Calculate maximum speed on a railway curve given
- superelevation (cant)
- cant deficiency
- curve radius
"""

import math

def max_curve_speed(radius_m,
                    cant_mm=180,
                    cant_def_mm=150,
                    gauge_mm=1500,
                    g=9.80665):
    """
    Calculate maximum speed (km/h) on a railway curve.

    Parameters:
    - radius_m    : Curve radius in meters
    - cant_mm     : Superelevation (cant) in millimeters (default 180)
    - cant_def_mm : Maximum cant deficiency in millimeters (default 150)
    - gauge_mm    : Track gauge (rail centerline-rail centerline) in millimeters (default 1500)
    - g           : Gravitational acceleration in m/s² (default 9.80665)

    Returns:
    - v_kmh : Maximum speed in km/h
    """
    # Convert mm to meters
    c0 = cant_mm / 1000.0
    u0 = cant_def_mm / 1000.0
    b  = gauge_mm / 1000.0

    # speed in m/s
    v_ms = math.sqrt((c0 + u0) * g * radius_m / b)
    # convert to km/h
    v_kmh = v_ms * 3.6
    return v_kmh

def main():
    print("Max Curve Speed Calculator")
    try:
        R = float(input("Enter curve radius R (m): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for radius.")
        return

    # Optionally, allow user to override defaults
    override = input("Use default cant 180 mm & cant deficiency 150 mm? (Y/n): ").strip().lower()
    if override == 'n':
        cant = float(input(" Enter cant (mm): "))
        cant_def = float(input(" Enter cant deficiency (mm): "))
    else:
        cant = 180.0
        cant_def = 150.0

    # Compute
    v = max_curve_speed(radius_m=R, cant_mm=cant, cant_def_mm=cant_def)
    print(f"\nFor R = {R:.1f} m, cant = {cant:.1f} mm, cant deficiency = {cant_def:.1f} mm:")
    print(f" Maximum permissible speed: {v:.2f} km/h ({v * 0.621371:.2f} mph)")

if __name__ == "__main__":
    main()
