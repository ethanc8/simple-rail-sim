name = 'Stadler FLIRT Akku (NAH.SH)'

# https://dt5online.de/regionalverkehr/stadler-flirt-akku/
# https://www.stadlerrail.com/api/docs/x/5aa4c05888/flirt-akku-nahsh_en.pdf
power_weight_ratio  = 10     # kW per tonne → power/weight ratio

# Assume same as normal FLIRT
initial_accel       = 1.2       # initial max accel (m/s²)
# https://www.stadlerrail.com/api/docs/x/feee1f1a47/fakku1222e.pdf
max_speed           = 140       # max speed (km/h)

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

