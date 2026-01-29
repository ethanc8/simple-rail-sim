from units import *
name = 'Siemens Velaro Novo'

# Data is from https://assets.new.siemens.com/siemens/assets/api/uuid:fe879294-8094-4f10-a45a-1d51509e5800/backgrounder-velaronovo-e.pdf
power_weight_ratio  = 19.04 * kW/t # kW per tonne → power/weight ratio
initial_accel       = 0.65 * m/(s**2)   # initial max accel (m/s²)
max_speed           = 360 * km/h   # max speed (km/h)

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
c_coef = 0.000022       # Running resistance c (quadratic)
