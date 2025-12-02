from units import *

name = 'Amtrak Midwest - Siemens Charger with 5 railcars'

# Calculate power-weight ratio
power = 3300 * kW # Siemens Charger SC-44
locomotive_mass = 120 * t
empty_railcar_mass = 50.802 * t
average_person_mass = 0.08405 * t
total_mass = locomotive_mass + 5*(empty_railcar_mass + 60*average_person_mass)

power_weight_ratio  = power/total_mass     # kW per tonne → power/weight ratio
initial_accel       = 0.3 * m/(s**2)       # initial max accel (m/s²)
max_speed           = 200 * km/h       # max speed (m/s)

# Running resistance (m/s)
# The acceleration caused by running resistance is calculated as
#   a_res = a + bv + cv^2.

# Many datasheets provide coefficients for calculating the force caused by running resistance
#   F_res = A + Bv + Cv^2.
# Since F=ma, you can divide by the mass of the entire trainset in order to find
# the running resistance coefficients for acceleration caused by running resistance.

# These values are from the following paper:
# https://web.archive.org/web/20161027012301if_/https://www.ave.kth.se/polopoly_fs/1.178975!/Menu/general/column-content/attachment/Tiliting%20trains.pdf
# They apply to the X 2000, but the effect is negligible below 160 km/h.

a_coef = 0.0059         # Running resistance a (constant)
b_coef = 0.000118       # Running resistance b (linear)
c_coef = 0.000022       # Running resistance c (quadratic)

