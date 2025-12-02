scenario_name = "BNSF Line - current peak locals"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmbnsf.html
# Speed limits are from OpenRailwayMap

route = [
                                # CHICAGO LASALLE ST stop
    (  0.0*mi,    0.3*mi, 10*mi/h, False, dwell_time),
    # We assume it gets up to 55mph pretty quickly, otherwise it'd be good to upgrade the tracks there
    (  0.3*mi,    1.8*mi, 55*mi/h, False, dwell_time),
    # This part is completely straight, there's no reason we need to go 55mph
    # but that's apparently the limit according to grade crossing inventories.
    # If it's track condition the tracks should be upgraded
    (  1.8*mi,    3.1*mi, 55*mi/h, True, dwell_time),
                                # 35TH STREET stop
    (  3.1*mi,    3.7*mi, 55*mi/h, False, dwell_time),
    (  3.7*mi,    7.5*mi, 70*mi/h, False, dwell_time),
    (  7.5*mi,    8.8*mi, 79*mi/h, True, dwell_time),
                                # AUBURN PARK stop
    (  8.8*mi,    9.8*mi, 79*mi/h, True, dwell_time),
                                # GRESHAM stop
    (  9.8*mi,    9.9*mi, 79*mi/h, False, dwell_time),
                                # Gresham Junction
                                # begin Beverly Branch
    (  9.9*mi,   10.6*mi, 30*mi/h, True, dwell_time),
                                # BRAINERD stop
    ( 10.6*mi,   11.3*mi, 30*mi/h, True, dwell_time),
                                # BEVERLY HILLS-91ST STREET stop
    ( 11.3*mi,   11.7*mi, 30*mi/h, True, dwell_time),
                                # BEVERLY HILLS-95TH STREET stop
    ( 11.7*mi,   12.3*mi, 30*mi/h, True, dwell_time),
                                # BEVERLY HILLS-99TH STREET stop
    ( 12.3*mi,   12.8*mi, 30*mi/h, True, dwell_time),
                                # BEVERLY HILLS-103RD STREET stop
    ( 12.8*mi,   13.3*mi, 30*mi/h, True, dwell_time),
                                # BEVERLY HILLS-107TH STREET stop
    ( 13.3*mi,   13.8*mi, 30*mi/h, True, dwell_time),
                                # MORGAN PARK-111TH STREET stop
    ( 13.8*mi,   14.3*mi, 30*mi/h, True, dwell_time),
                                # MORGAN PARK-115TH STREET stop
    ( 14.3*mi,   14.8*mi, 30*mi/h, True, dwell_time),
                                # BLUE ISLAND-119TH STREET stop
    ( 14.8*mi,   15.2*mi, 30*mi/h, True, dwell_time),
                                # BLUE ISLAND-123RD STREET stop
    ( 15.2*mi,   15.9*mi, 30*mi/h, True, dwell_time),
                                # BLUE ISLAND-PRAIRIE STREET stop
    ( 15.9*mi,   16.4*mi, 30*mi/h, True, dwell_time),
                                # BLUE ISLAND-VERMONT STREET stop
]

stops = {
    0.0*mi: 'Chicago - LaSalle St',
    3.1*mi: '35th St',
    8.8*mi: 'Auburn Park',
    9.8*mi: 'Gresham',
    10.6*mi: 'Brainerd',
    11.3*mi: 'Beverly Hills - 91st St',
    11.7*mi: 'Beverly Hills - 95th St',
    12.3*mi: 'Beverly Hills - 99th St',
    12.8*mi: 'Beverly Hills - 103rd St',
    13.3*mi: 'Beverly Hills - 107th St',
    13.8*mi: 'Morgan Park - 111th St',
    14.3*mi: 'Morgan Park - 115th St',
    14.8*mi: 'Blue Island - 119th St',
    15.2*mi: 'Blue Island - 123rd St',
    15.9*mi: 'Blue Island - Prairie St',
    16.4*mi: 'Blue Island - Vermont St',
}

dwell_time = 45 # seconds
