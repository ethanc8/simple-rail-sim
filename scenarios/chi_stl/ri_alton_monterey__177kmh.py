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

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# We assume that the RID, the former Alton RR from Joliet to the junction with 
# the Monterey Sub, and the Monterey Sub are all upgraded to allow 177 km/h 
# operation throughout. If this is not possible then travel times will be affected,
# but it shouldn't be too much of a problem.
route = [
                                # CHICAGO LASALLE ST stop
    (rid(0.0)*mi,  rid(40.2)*mi, 177*km/h, True, dwell_time),
                                # JOLIET stop
    (alton( 37.2)*mi,  alton(  72.8)*mi, 177*km/h, True, dwell_time),
                                # DWIGHT stop
    (alton( 72.8)*mi,  alton(  92.5)*mi, 177*km/h, True, dwell_time),
                                # PONTIAC stop
    (alton( 92.5)*mi,  alton( 124.1)*mi, 177*km/h, True, dwell_time),
                                # BLOOMINGTON-NORMAL stop
    (alton(124.1)*mi,  alton( 156.4)*mi, 177*km/h, True, dwell_time),
                                # LINCOLN stop
    (alton(156.4)*mi,  alton( 185.1)*mi, 177*km/h, True, dwell_time),
                                # SPRINGFIELD stop
    (alton(185.1)*mi,  alton( 213.0)*mi, 177*km/h, False, dwell_time),
    (monterey(88.9)*mi,  monterey(119.2)*mi, 177*km/h, False, dwell_time),
    (brooklyn(452.1)*mi,  brooklyn(468.0)*mi, 177*km/h, True, dwell_time),
                                # EDWARDSVILLE stop
                                # This is a new station
    (brooklyn(468.0)*mi,  brooklyn(474.7)*mi, 177*km/h, False, dwell_time),

    # From here on we build a high-speed route between the UP and NS tracks; we might need to relocate some tracks.
    # I have not verified if the existing curves are suitable for 177 km/h operation
    # If they are not, it's probably not feasible to straighten them
    (brooklyn(474.7)*mi,  brooklyn(485.0)*mi, 177*km/h, False, dwell_time),
    
    # And then we build a new 177 km/h bridge across the river
    # a bit north of the MacArthur bridge
    # Assume we just build immediately north of the TRRA alignment for now
    (brooklyn(485.0)*mi,  trra(1.5)*mi, 177*km/h, False, dwell_time),
    (trra(1.5)*mi,  trra(0.0)*mi, 100*km/h, True, dwell_time),
                                # ST. LOUIS stop
]

stops = {
    0.0*mi: 'Chicago LaSalle Street',
    alton(37.2)*mi: 'Joliet',
    alton(72.8)*mi: 'Dwight',
    alton(92.5)*mi: 'Pontiac',
    alton(124.1)*mi: 'Bloomington-Normal',
    alton(156.4)*mi: 'Lincoln',
    alton(185.1)*mi: 'Springfield',
    brooklyn(468.0)*mi: 'Edwardsville',
    trra(0.0)*mi: 'St. Louis'
}

dwell_time = 60 # seconds
