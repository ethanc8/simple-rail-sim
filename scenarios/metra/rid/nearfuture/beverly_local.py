scenario_name = "BNSF Line - current peak locals"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmbnsf.html
# Speed limits are from OpenRailwayMap

route = [
                                # CHICAGO LASALLE ST stop
    (  0.0,   0.3, mph(10), False),
    # We assume it gets up to 55mph pretty quickly, otherwise it'd be good to upgrade the tracks there
    (  0.3,   1.8, mph(55), False),
    # This part is completely straight, there's no reason we need to go 55mph
    # but that's apparently the limit according to grade crossing inventories.
    # If it's track condition the tracks should be upgraded
    (  1.8,   3.1, mph(55), True),
                                # 35TH STREET stop
    (  3.1,   3.7, mph(55), False),
    (  3.7,   7.5, mph(70), False),
    (  7.5,   8.8, mph(79), True),
                                # AUBURN PARK stop
    (  8.8,   9.8, mph(79), True),
                                # GRESHAM stop
    (  9.8,   9.9, mph(79), False),
                                # Gresham Junction
                                # begin Beverly Branch
    (  9.9,  10.6, mph(30), True),
                                # BRAINERD stop
    ( 10.6,  11.3, mph(30), True),
                                # BEVERLY HILLS-91ST STREET stop
    ( 11.3,  11.7, mph(30), True),
                                # BEVERLY HILLS-95TH STREET stop
    ( 11.7,  12.3, mph(30), True),
                                # BEVERLY HILLS-99TH STREET stop
    ( 12.3,  12.8, mph(30), True),
                                # BEVERLY HILLS-103RD STREET stop
    ( 12.8,  13.3, mph(30), True),
                                # BEVERLY HILLS-107TH STREET stop
    ( 13.3,  13.8, mph(30), True),
                                # MORGAN PARK-111TH STREET stop
    ( 13.8,  14.3, mph(30), True),
                                # MORGAN PARK-115TH STREET stop
    ( 14.3,  14.8, mph(30), True),
                                # BLUE ISLAND-119TH STREET stop
    ( 14.8,  15.2, mph(30), True),
                                # BLUE ISLAND-123RD STREET stop
    ( 15.2,  15.9, mph(30), True),
                                # BLUE ISLAND-PRAIRIE STREET stop
    ( 15.9,  16.4, mph(30), True),
                                # BLUE ISLAND-VERMONT STREET stop
]

stops = {
    0.0: 'Chicago - LaSalle St',
    3.1: '35th St',
    8.8: 'Auburn Park',
    9.8: 'Gresham',
    10.6: 'Brainerd',
    11.3: 'Beverly Hills - 91st St',
    11.7: 'Beverly Hills - 95th St',
    12.3: 'Beverly Hills - 99th St',
    12.8: 'Beverly Hills - 103rd St',
    13.3: 'Beverly Hills - 107th St',
    13.8: 'Morgan Park - 111th St',
    14.3: 'Morgan Park - 115th St',
    14.8: 'Blue Island - 119th St',
    15.2: 'Blue Island - 123rd St',
    15.9: 'Blue Island - Prairie St',
    16.4: 'Blue Island - Vermont St',
}

dwell_time = 45 # seconds
