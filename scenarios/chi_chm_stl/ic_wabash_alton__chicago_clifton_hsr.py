scenario_name = "IC-Wabash-Alton (300 km/h Chicago-Clifton)"

def wabash(mp):
    # Wabash MP 338.0 = IC MP 137.1 (Tolono)
    return (mp - 338.0 + 137.1)

def alton(mp):
    # Alton MP 187.4 = Wabash MP 416.5 (Iles)
    return wabash(mp - 187.4 + 416.5)

def alton_orig(mp):
    # Between Godfrey and Wann, a cutoff was built
    # At Wann, Alton (cutoff) MP 259.6 = Alton (original) MP 262.1
    return alton(mp - 262.1 + 259.6)

def trra(mp):
    # TRRA MP 3.3 = Alton (orig) MP 281.0 (Q Tower)
    # But they go down as you approach St Louis
    return alton_orig((3.3 - mp) + 281.0)

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0,   3.0, 100, False), # St Charles Air Line
    (  3.0,   4.1, 150, False), # 34th St curve, and some minor curves
    (  4.2,   5.9, 300, False),
    (  5.9,   7.2, 250, False), # Hyde Park curve
    (  7.2,  16.5, 300, False), 
    ( 16.5,  17.0, 250, False), # 133rd St curve
    ( 17.0,  47.9, 300, False),
    ( 47.9,  48.4, 280, False), # Manteno curve
    ( 48.4,  55.9, 300, True),
                                # KANKAKEE stop
    ( 55.9,  67.4, 300, False), # 5100 N Rd grade crossing, Clifton
    ( 67.4, 127.8, 177, True ), 
                                # CHAMPAIGN stop
    (127.8, 137.0, 177, False),
    (137.0, wabash(338.1), 100, False),  # Tolono - switch from IC Main Line to Wabash (NS Lafayette District)
    # TODO: Is this a reasonable assumption for the speed around the curve in Tolono?
    # TODO: Calculate curve radii west of Tolono

    (wabash(338.1), wabash(376), 177, True),
                                # DECATUR stop
                                # This is a new station
    (wabash(376), wabash(414.3), 177, True),
                                # SPRINGFIELD stop
                                # This is the new Springfield-Sangamon Transportation Center
    (wabash(414.3), wabash(416.5), 177, False),
                                # At Iles junction, switch to the former Alton RR (UP Springfield Sub)
    (alton(187.4), alton(256.8), 177, False),
                                # skip ALTON station
                                # Joliet to Alton station has already been upgraded to 177 km/h
    (256.8, 259.6, 145, False),
    (alton_orig(262.1), alton_orig(270.0), 145, False),
    (alton_orig(270.0), alton_orig(274.4), 145, False),
    (alton_orig(274.4), trra(1.5), 40, True),
                                # ST. LOUIS stop
]

stops = {
    0.0: 'Chicago Union Station',
    55.9: 'Kankakee',
    127.8: 'Champaign',
    wabash(376): 'Decatur',
    wabash(414.3): 'Springfield',
    trra(1.5): 'St. Louis',
}

dwell_time = 60 # seconds
