from units import *
name = 'Highliner II'

average_person_mass = 0.08405 * t
railcar_mass = 67 * t + 150 * average_person_mass
# A typical gallery car has a capacity of 153-161 people
railcar_power = 600 * kW

# https://pedestrianobservations.com/2018/06/28/the-value-of-modern-emus/
# Power-weight ratio is 21.1 kW/t, without passengers
#   (https://documents.epfl.ch/users/a/al/allenbac/www/documents/Fich0321.pdf)
# Adding the mass of passengers reduces it to around 20
power_weight_ratio  = railcar_power/railcar_mass     # kW per tonne → power/weight ratio

# https://documents.epfl.ch/users/a/al/allenbac/www/documents/Fich0321.pdf
initial_accel       = 0.581 * m/(s**2)       # initial max accel (m/s²)
max_speed           = 90 * mi/h       # max speed (m/s)

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

