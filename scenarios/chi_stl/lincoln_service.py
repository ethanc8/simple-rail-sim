scenario_name = "IC Main Line (177 km/h)"

def alton_orig(mp):
    # Between Godfrey and Wann, a cutoff was built
    # At Wann, Alton (cutoff) MP 259.6 = Alton (original) MP 262.1
    return mp - 262.1 + 259.6

def trra(mp):
    # TRRA MP 9.0 = Alton (orig) MP 274.4 (WR Tower) + 0.7 miles
    # But they go down as you approach St Louis
    return alton_orig((9.0 - mp) + 274.4 + 0.7)

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Joliet-Alton was upgraded to 110 mph (177 km/h) recently
# Other speeds are found from grade crossing inventory reports
#   (https://experience.arcgis.com/experience/b6c12fd0a4774f38a303e3d034775854/)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0,   2.0,  40, False), # 25 mph access to CUS
    (  2.0,   3.5,  65, False), # 40 mph shared with BNSF
    (  3.5,  11.9, 127, True),
                                # SUMMIT stop
    ( 11.9,  37.2, 127, True),
                                # JOLIET stop
    ( 37.2,  72.8, 177, True),
                                # DWIGHT stop
    ( 72.8,  92.5, 177, True),
                                # PONTIAC stop
    ( 92.5, 124.1, 177, True),
                                # BLOOMINGTON-NORMAL stop
    (124.1, 156.4, 177, True),
                                # LINCOLN stop
    (156.4, 185.1, 177, True),
                                # SPRINGFIELD stop
    (185.1, 223.8, 177, True),
                                # CARLINVILLE stop
    (223.8, 256.8, 177, True),
                                # ALTON stop
    (256.8, 259.6, 145, False),
    (alton_orig(262.1), alton_orig(270.0), 145, False),
    (alton_orig(270.0), alton_orig(274.4), 145, False),
    (alton_orig(274.4), trra(1.5), 40, True),
                                # ST. LOUIS stop
]

stops = {
    0.0: 'Chicago Union Station',
    11.9: 'Summit',
    37.2: 'Joliet',
    72.8: 'Dwight',
    92.5: 'Pontiac',
    124.1: 'Bloomington-Normal',
    156.4: 'Lincoln',
    185.1: 'Springfield',
    223.8: 'Carlinville',
    256.8: 'Alton',
    trra(1.5): 'St. Louis',
}
