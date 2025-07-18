scenario_name = "IC Main Line (300 km/h Chicago-Clifton)"

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)
route = [
                                # CHICAGO UNION STATION stop
    (  0.0,   3.0, 100, False), # St Charles Air Line
    (  3.0,   4.1, 150, False), # 34th St curve, and some minor curves
    (  4.2,   5.9, 300, False),
    (  5.9,   7.2, 250, False), # Hyde Park curve
    (  7.2,  16.5, 300, False), 
    ( 16.5,  17.0, 250, False), # 133rd St curve
    ( 17.0,  38.9, 300, False), # North Peotone Rd grade crossing, Peotone
    ( 38.9,  47.9, 177, False),
    ( 47.9,  48.4, 177, False), # Manteno curve
    ( 48.4,  55.9, 177, True),
                                # KANKAKEE stop
    ( 55.9,  67.4, 177, False), # 5100 N Rd grade crossing, Clifton
    ( 67.4, 127.8, 177, True ), 
                                # CHAMPAIGN stop
]

stops = {
    0.0: 'Chicago Union Station',
    55.9: 'Kankakee',
    127.8: 'Champaign'
}

dwell_time = 60 # seconds
