scenario_name = "Lincoln Service - current"

def alton_orig(mp):
    # Between Godfrey and Wann, a cutoff was built
    # At Wann, Alton (cutoff) MP 259.6 = Alton (original) MP 262.1
    return mp - 262.1 + 259.6

def trra(mp):
    # TRRA MP 9.0 = Alton (orig) MP 274.4 (WR Tower) + 0.7 miles
    # But they go down as you approach St Louis
    return alton_orig((9.0 - mp) + 274.4 + 0.7)

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Joliet-Alton was partially upgraded to 110 mph (177 km/h) recently
#   sources for which parts: OpenRailwayMap, reports and articles found by ChatGPT
#   (https://chatgpt.com/c/6878645b-8274-8013-8723-880cc81d18d3)
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
    ( 37.2,  40.0, 105, False), # exiting Joliet
    ( 40.0,  45.6, 177, False),
    ( 45.6,  46.0, 129, False), # Elwood curve
    ( 46.0,  52.0, 177, False),
    ( 52.0,  53.0, 113, False), # Wilmington curve and bridge
    ( 53.0,  72.5, 177, False),
    ( 72.5,  72.8,  80, False), # Crossing NS Kankakee Branch
    ( 72.8,  73.8, 177, True),
                                # DWIGHT stop
    ( 73.8,  77.5, 177, False),
    ( 77.5,  77.8, 161, False), # Dwight-Odell curve and short bridge
    ( 77.8,  91.1, 177, False),
    ( 91.1,  91.3, 129, False), # Pontiac curve
    ( 91.3,  92.5, 177, True),
                                # PONTIAC stop
    ( 92.5, 109.5, 177, False),
    (109.5, 109.9, 153, False), # Lexington curve
    (109.9, 123.0, 177, False),
    (123.0, 124.1,  80, True),
                                # BLOOMINGTON-NORMAL stop
    (124.1, 126.6,  80, False),
    (126.6, 130.3, 177, False),
    (130.3, 130.6, 153, False), # Shirley curve
    (130.6, 145.6, 177, False),
    (145.6, 146.0, 137, False), # First Atlanta curve
    (146.0, 149.0, 153, False), # Second and third Atlanta curve
    (149.0, 156.4, 177, True),
                                # LINCOLN stop
    (156.4, 157.0, 177, False),
    (157.0, 157.5, 153, False), # Lincoln curve
    (157.5, 185.1, 177, True),
                                # SPRINGFIELD stop
    (185.1, 187.4,  97, False),
    (187.4, 223.8, 177, True),
                                # CARLINVILLE stop
    (223.8, 256.8, 130, True),
                                # ALTON stop
    # Parts of Carlinville-Alton are 110 mph (177 km/h)
    # but it's very curvy. The fastest timetabled time is 25 min.
    (256.8, 259.6, 145, False),
    (alton_orig(262.1), alton_orig(270.0), 145, False),
    (alton_orig(270.0), alton_orig(274.4), 145, False),
    (alton_orig(274.4), trra(1.5), 40, True),
                                # ST. LOUIS stop
    # In reality it takes at ~45 min (timetabled) to get to STL from Alton.
]

stops = {
    0.0: 'Chicago Union Station',
    11.9: 'Summit',
    37.2: 'Joliet',
    73.8: 'Dwight',
    92.5: 'Pontiac',
    124.1: 'Bloomington-Normal',
    156.4: 'Lincoln',
    185.1: 'Springfield',
    223.8: 'Carlinville',
    256.8: 'Alton',
    trra(1.5): 'St. Louis',
}
