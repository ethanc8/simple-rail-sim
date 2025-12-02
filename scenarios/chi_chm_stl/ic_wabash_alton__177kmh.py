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

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0*mi,    3.0*mi, 100*km/h, False, dwell_time), # St Charles Air Line
    (  3.0*mi,    4.1*mi, 150*km/h, False, dwell_time), # 34th St curve, and some minor curves
    (  4.2*mi,    5.9*mi, 177*km/h, False, dwell_time),
    (  5.9*mi,    7.2*mi, 177*km/h, False, dwell_time), # Hyde Park curve
    (  7.2*mi,   16.5*mi, 177*km/h, False, dwell_time), 
    ( 16.5*mi,   17.0*mi, 177*km/h, False, dwell_time), # 133rd St curve
    ( 17.0*mi,   47.9*mi, 177*km/h, False, dwell_time),
    ( 47.9*mi,   48.4*mi, 177*km/h, False, dwell_time), # Manteno curve
    ( 48.4*mi,   55.9*mi, 177*km/h, True, dwell_time),
                                # KANKAKEE stop
    ( 55.9*mi,   67.4*mi, 177*km/h, False, dwell_time), # 5100 N Rd grade crossing, Clifton
    ( 67.4, 127.8, 177, True ), 
                                # CHAMPAIGN stop
    (127.8*mi,  137.0*mi, 177*km/h, False, dwell_time),
    (137.0*mi,  wabash(338.1)*mi, 100*km/h, False, dwell_time),  # Tolono - switch from IC Main Line to Wabash (NS Lafayette District)
    # TODO: Is this a reasonable assumption for the speed around the curve in Tolono?
    # TODO: Calculate curve radii west of Tolono

    (wabash(338.1)*mi,  wabash(376)*mi, 177*km/h, True, dwell_time),
                                # DECATUR stop
                                # This is a new station
    (wabash(376)*mi,  wabash(414.3)*mi, 177*km/h, True, dwell_time),
                                # SPRINGFIELD stop
                                # This is the new Springfield-Sangamon Transportation Center
    (wabash(414.3)*mi,  wabash(416.5)*mi, 177*km/h, False, dwell_time),
                                # At Iles junction, switch to the former Alton RR (UP Springfield Sub)
    (alton(187.4)*mi,  alton(256.8)*mi, 177*km/h, False, dwell_time),
                                # skip ALTON station
                                # Joliet to Alton station has already been upgraded to 177 km/h
    (256.8*mi,  259.6*mi, 145*km/h, False, dwell_time),
    (alton_orig(262.1)*mi,  alton_orig(270.0)*mi, 145*km/h, False, dwell_time),
    (alton_orig(270.0)*mi,  alton_orig(274.4)*mi, 145*km/h, False, dwell_time),
    (alton_orig(274.4)*mi,  trra(1.5)*mi, 40*km/h, True, dwell_time),
                                # ST. LOUIS stop
]

stops = {
    0.0*mi: 'Chicago Union Station',
    55.9*mi: 'Kankakee',
    127.8*mi: 'Champaign',
    wabash(376)*mi: 'Decatur',
    wabash(414.3)*mi: 'Springfield',
    trra(1.5)*mi: 'St. Louis',
}

dwell_time = 60 # seconds
