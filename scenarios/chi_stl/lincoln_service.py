scenario_name = "Lincoln Service - current"

def alton_orig(mp):
    # Between Godfrey and Wann, a cutoff was built
    # At Wann, Alton (cutoff) MP 259.6 = Alton (original) MP 262.1
    return mp - 262.1 + 259.6

def trra(mp):
    # TRRA MP 9.0 = Alton (orig) MP 274.4 (WR Tower) + 0.7 miles
    # But they go down as you approach St Louis
    return alton_orig((9.0 - mp) + 274.4 + 0.7)

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Joliet-Alton was partially upgraded to 110 mph (177 km/h) recently
#   sources for which parts: OpenRailwayMap, reports and articles found by ChatGPT
#   (https://chatgpt.com/c/6878645b-8274-8013-8723-880cc81d18d3)
# Other speeds are found from grade crossing inventory reports
#   (https://experience.arcgis.com/experience/b6c12fd0a4774f38a303e3d034775854/)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0*mi,    2.0*mi, 40*km/h, False, dwell_time), # 25 mph access to CUS
    (  2.0*mi,    3.5*mi, 65*km/h, False, dwell_time), # 40 mph shared with BNSF
    (  3.5*mi,   11.9*mi, 127*km/h, True, dwell_time),
                                # SUMMIT stop
    ( 11.9*mi,   37.2*mi, 127*km/h, True, dwell_time),
                                # JOLIET stop
    ( 37.2*mi,   40.0*mi, 105*km/h, False, dwell_time), # exiting Joliet
    ( 40.0*mi,   45.6*mi, 177*km/h, False, dwell_time),
    ( 45.6*mi,   46.0*mi, 129*km/h, False, dwell_time), # Elwood curve
    ( 46.0*mi,   52.0*mi, 177*km/h, False, dwell_time),
    ( 52.0*mi,   53.0*mi, 113*km/h, False, dwell_time), # Wilmington curve and bridge
    ( 53.0*mi,   72.5*mi, 177*km/h, False, dwell_time),
    ( 72.5*mi,   72.8*mi, 80*km/h, False, dwell_time), # Crossing NS Kankakee Branch
    ( 72.8*mi,   73.8*mi, 177*km/h, True, dwell_time),
                                # DWIGHT stop
    ( 73.8*mi,   77.5*mi, 177*km/h, False, dwell_time),
    ( 77.5*mi,   77.8*mi, 161*km/h, False, dwell_time), # Dwight-Odell curve and short bridge
    ( 77.8*mi,   91.1*mi, 177*km/h, False, dwell_time),
    ( 91.1*mi,   91.3*mi, 129*km/h, False, dwell_time), # Pontiac curve
    ( 91.3*mi,   92.5*mi, 177*km/h, True, dwell_time),
                                # PONTIAC stop
    ( 92.5*mi,  109.5*mi, 177*km/h, False, dwell_time),
    (109.5*mi,  109.9*mi, 153*km/h, False, dwell_time), # Lexington curve
    (109.9*mi,  123.0*mi, 177*km/h, False, dwell_time),
    (123.0*mi,  124.1*mi, 80*km/h, True, dwell_time),
                                # BLOOMINGTON-NORMAL stop
    (124.1*mi,  126.6*mi, 80*km/h, False, dwell_time),
    (126.6*mi,  130.3*mi, 177*km/h, False, dwell_time),
    (130.3*mi,  130.6*mi, 153*km/h, False, dwell_time), # Shirley curve
    (130.6*mi,  145.6*mi, 177*km/h, False, dwell_time),
    (145.6*mi,  146.0*mi, 137*km/h, False, dwell_time), # First Atlanta curve
    (146.0*mi,  149.0*mi, 153*km/h, False, dwell_time), # Second and third Atlanta curve
    (149.0*mi,  156.4*mi, 177*km/h, True, dwell_time),
                                # LINCOLN stop
    (156.4*mi,  157.0*mi, 177*km/h, False, dwell_time),
    (157.0*mi,  157.5*mi, 153*km/h, False, dwell_time), # Lincoln curve
    (157.5*mi,  185.1*mi, 177*km/h, True, dwell_time),
                                # SPRINGFIELD stop
    (185.1*mi,  187.4*mi, 97*km/h, False, dwell_time),
    (187.4*mi,  223.8*mi, 177*km/h, True, dwell_time),
                                # CARLINVILLE stop
    (223.8*mi,  256.8*mi, 130*km/h, True, dwell_time),
                                # ALTON stop
    # Parts of Carlinville-Alton are 110 mph (177 km/h)
    # but it's very curvy. The fastest timetabled time is 25 min.
    (256.8*mi,  259.6*mi, 145*km/h, False, dwell_time),
    (alton_orig(262.1)*mi,  alton_orig(270.0)*mi, 145*km/h, False, dwell_time),
    (alton_orig(270.0)*mi,  alton_orig(274.4)*mi, 145*km/h, False, dwell_time),
    (alton_orig(274.4)*mi,  trra(1.5)*mi, 40*km/h, True, dwell_time),
                                # ST. LOUIS stop
    # In reality it takes at ~45 min (timetabled) to get to STL from Alton.
]

stops = {
    0.0*mi: 'Chicago Union Station',
    11.9*mi: 'Summit',
    37.2*mi: 'Joliet',
    73.8*mi: 'Dwight',
    92.5*mi: 'Pontiac',
    124.1*mi: 'Bloomington-Normal',
    156.4*mi: 'Lincoln',
    185.1*mi: 'Springfield',
    223.8*mi: 'Carlinville',
    256.8*mi: 'Alton',
    trra(1.5)*mi: 'St. Louis',
}

dwell_time = 60 # seconds
