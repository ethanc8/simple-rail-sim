scenario_name = "CHI-STL via RID, Alton RR, Monterey Sub, and Brooklyn District (177 km/h)"

def rid(mp):
    return mp

def alton(mp):
    # At Joliet, RID MP 40.2 = Alton MP 37.2
    return rid(mp - 37.2 + 40.2)

def monterey(mp):
    # At Nilwood, Alton MP 213.0 = Monterey Sub MP 88.9
    return alton(mp - 88.9 + 213.0)

def brooklyn(mp):
    # At Staunton (DeCamp Jct), Monterey Sub MP 119.2 = Brooklyn District MP 452.1
    return monterey(mp - 452.1 + 119.2)

def trra(mp):
    # At Q Tower, TRRA MP 3.3 = Brooklyn District MP 486.0
    # But they go down as you approach St Louis
    return brooklyn((3.3 - mp) + 486.0)

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# We assume that the RID, the former Alton RR from Joliet to the junction with 
# the Monterey Sub, and the Monterey Sub are all upgraded to allow 177 km/h 
# operation throughout. If this is not possible then travel times will be affected,
# but it shouldn't be too much of a problem.
route = [
                                # CHICAGO LASALLE ST stop
    (rid(0.0), rid(40.2), 177, True),
                                # JOLIET stop
    (alton( 37.2), alton(  72.8), 177, True),
                                # DWIGHT stop
    (alton( 72.8), alton(  92.5), 177, True),
                                # PONTIAC stop
    (alton( 92.5), alton( 124.1), 177, True),
                                # BLOOMINGTON-NORMAL stop
    (alton(124.1), alton( 156.4), 177, True),
                                # LINCOLN stop
    (alton(156.4), alton( 185.1), 177, True),
                                # SPRINGFIELD stop
    (alton(185.1), alton( 213.0), 177, False),
    (monterey(88.9), monterey(119.2), 177, False),
    (brooklyn(452.1), brooklyn(468.0), 177, True),
                                # EDWARDSVILLE stop
                                # This is a new station
    (brooklyn(468.0), brooklyn(474.7), 177, False),

    # From here on we build a high-speed route between the UP and NS tracks; we might need to relocate some tracks.
    # I have not verified if the existing curves are suitable for 177 km/h operation
    # If they are not, it's probably not feasible to straighten them
    (brooklyn(474.7), brooklyn(485.0), 177, False),
    
    # And then we build a new 177 km/h bridge across the river
    # a bit north of the MacArthur bridge
    # Assume we just build immediately north of the TRRA alignment for now
    (brooklyn(485.0), trra(1.5), 177, False),
    (trra(1.5), trra(0.0), 100, True),
                                # ST. LOUIS stop
]

stops = {
    0.0: 'Chicago LaSalle Street',
    alton(37.2): 'Joliet',
    alton(72.8): 'Dwight',
    alton(92.5): 'Pontiac',
    alton(124.1): 'Bloomington-Normal',
    alton(156.4): 'Lincoln',
    alton(185.1): 'Springfield',
    brooklyn(468.0): 'Edwardsville',
    trra(0.0): 'St. Louis'
}

dwell_time = 60 # seconds
