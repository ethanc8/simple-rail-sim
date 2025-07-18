scenario_name = "BNSF Line - semi-express to Kendall"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmbnsf.html
# Speed limits are from OpenRailwayMap

route = [
                                # CHICAGO UNION STATION stop
    (  0.0,   0.6, mph(15), False),
    (  0.6,   0.8, mph(30), False),
    (  0.8,   1.4, mph(25), False),
    (  1.4,   1.8, mph(35), False),
                                # skip HALSTED ST stop
    (  1.8,   2.3, mph(40), False),
    (  2.3,   3.7, mph(60), False),
                                # skip WESTERN AVE
    (  3.7,  13.0, mph(70), False),
                                # skip the rest of zone 2
                                # skip CONGRESS PARK
    ( 13.0,  13.7, mph(70), False),
                                # skip LA GRANGE RD
    ( 13.7,  14.0, mph(70), False),
                                # skip STONE AVE stop
    ( 14.0,  15.4, mph(70), True),
                                # WESTERN SPRINGS
    ( 15.4,  16.3, mph(70), False),
                                # skip HIGHLANDS
    ( 16.3,  16.8, mph(70), True),
                                # HINSDALE stop
    ( 16.8,  17.7, mph(70), False),
                                # skip WEST HINSDALE
    ( 17.7,  18.2, mph(70), False),
                                # skip CLARENDON HILLS
    ( 18.2,  19.5, mph(70), True),
                                # WESTMONT stop
    ( 19.5,  20.3, mph(70), False),
                                # skip FAIRVIEW AVE
    ( 20.3,  21.1, mph(70), True),
                                # DOWNERS GROVE stop
    ( 21.1,  22.8, mph(70), True),
                                # BELMONT stop
    ( 22.8,  24.4, mph(70), True),
                                # LISLE stop
    ( 24.4,  28.4, mph(70), True),
                                # NAPERVILLE stop
    ( 28.4,  31.7, mph(70), True),
                                # ROUTE 59 stop
    ( 31.7,  35.4, mph(70), False),
    ( 35.4,  37.4, mph(55), True),
                                # AURORA stop
    ( 37.4,  38.0, mph(55), False),
    ( 38.0,  39.0, mph(35), False),
    ( 39.0,  40.0, mph(75), True),
                                # MONTGOMERY stop
    ( 40.0,  43.3, mph(79), True),
                                # OSWEGO stop
                                # decently north of downtown Oswego
    ( 43.3,  48.5, mph(79), True),
                                # YORKVILLE stop
                                # decently north of downtown Yorkville
    ( 48.5,  52.7, mph(79), True),
                                # PLANO stop
                                # at Little Rock Rd, not in downtown Plano
    ( 52.7,  56.9, mph(79), True),
                                # SANDWICH stop
                                # at Fairwind Blvd, not in downtown Sandwich
]

stops = {
    0.0: 'Chicago Union Station',
    1.8: 'Halsted St',
    3.7: 'Western Ave',
    6.9: 'Cicero',
    9.0: 'LaVergne',
    9.5: 'Berwyn',
    10.1: 'Harlem Ave',
    11.0: 'Riverside',
    11.8: 'Hollywood',
    12.4: 'Brookfield',
    13.0: 'Congress Park',
    13.7: 'LaGrange Rd',
    14.0: 'Stone Ave',
    15.4: 'Western Springs',
    16.3: 'Highlands',
    16.8: 'Hinsdale',
    17.7: 'West Hinsdale',
    18.2: 'Clarendon Hills',
    19.5: 'Westmont',
    20.3: 'Fairview Ave.',
    21.1: 'Downers Grove',
    22.8: 'Belmont',
    24.4: 'Lisle',
    28.4: 'Naperville',
    31.7: 'Route 59',
    37.4: 'Aurora',
    40.0: 'Montgomery',
    43.3: 'Oswego',
    48.5: 'Yorkville',
    52.7: 'Plano',
    56.9: 'Sandwich'
}

dwell_time = 30 # seconds
