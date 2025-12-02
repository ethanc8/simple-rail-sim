from units import *
name = 'N700 Series Shinkansen'

# Power-weight ratio and initial acceleration are from
# https://pedestrianobservations.com/2018/06/28/the-value-of-modern-emus/
power_weight_ratio  = 26.74 * kW/t # kW per tonne → power/weight ratio
initial_accel       = 0.9 * m/(s**2)  # initial max accel (m/s²)
max_speed           = 300 * km/h  # max speed (m/s)

# Running resistance (m/s)
# The acceleration caused by running resistance is calculated as
#   a_res = a + bv + cv^2.

# Many datasheets provide coefficients for calculating the force caused by running resistance
#   F_res = A + Bv + Cv^2.
# Since F=ma, you can divide by the mass of the entire trainset in order to find
# the running resistance coefficients for acceleration caused by running resistance.

# These values are from the following paper:
# https://web.archive.org/web/20161027012301if_/https://www.ave.kth.se/polopoly_fs/1.178975!/Menu/general/column-content/attachment/Tiliting%20trains.pdf
# They apply to the X 2000, but it should be similar to other high-speed trainsets.
a_coef = 0.0059         # Running resistance a (constant)
b_coef = 0.000118       # Running resistance b (linear)

# This value was experimentally measured by Alon Levy.
# https://pedestrianobservations.com/2018/06/28/the-value-of-modern-emus/
c_coef = 0.000018       # Running resistance c (quadratic)

