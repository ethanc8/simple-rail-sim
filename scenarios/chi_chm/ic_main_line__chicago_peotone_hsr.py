scenario_name = "IC Main Line (300 km/h Chicago-Clifton)"

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0*mi,    3.0*mi, 100*km/h, False, dwell_time), # St Charles Air Line
    (  3.0*mi,    4.1*mi, 150*km/h, False, dwell_time), # 34th St curve, and some minor curves
    (  4.2*mi,    5.9*mi, 300*km/h, False, dwell_time),
    (  5.9*mi,    7.2*mi, 250*km/h, False, dwell_time), # Hyde Park curve
    (  7.2*mi,   16.5*mi, 300*km/h, False, dwell_time), 
    ( 16.5*mi,   17.0*mi, 250*km/h, False, dwell_time), # 133rd St curve
    ( 17.0*mi,   38.9*mi, 300*km/h, False, dwell_time), # North Peotone Rd grade crossing, Peotone
    ( 38.9*mi,   47.9*mi, 177*km/h, False, dwell_time),
    ( 47.9*mi,   48.4*mi, 177*km/h, False, dwell_time), # Manteno curve
    ( 48.4*mi,   55.9*mi, 177*km/h, True, dwell_time),
                                # KANKAKEE stop
    ( 55.9*mi,   67.4*mi, 177*km/h, False, dwell_time), # 5100 N Rd grade crossing, Clifton
    ( 67.4, 127.8, 177, True ), 
                                # CHAMPAIGN stop
]

stops = {
    0.0*mi: 'Chicago Union Station',
    55.9*mi: 'Kankakee',
    127.8*mi: 'Champaign'
}

dwell_time = 60 # seconds
