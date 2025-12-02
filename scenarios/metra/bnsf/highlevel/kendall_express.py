scenario_name = "BNSF Line - semi-express to Kendall"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmbnsf.html
# Speed limits are from OpenRailwayMap

route = [
                                # CHICAGO UNION STATION stop
    (  0.0*mi,    0.6*mi, 15*mi/h, False, dwell_time),
    (  0.6*mi,    0.8*mi, 30*mi/h, False, dwell_time),
    (  0.8*mi,    1.4*mi, 25*mi/h, False, dwell_time),
    (  1.4*mi,    1.8*mi, 35*mi/h, False, dwell_time),
                                # skip HALSTED ST stop
    (  1.8*mi,    2.3*mi, 40*mi/h, False, dwell_time),
    (  2.3*mi,    3.7*mi, 60*mi/h, False, dwell_time),
                                # skip WESTERN AVE
    (  3.7*mi,   35.4*mi, 70*mi/h, False, dwell_time),
                                # skip the rest of zones 2, 3, 4
    ( 35.4*mi,   37.4*mi, 55*mi/h, True, dwell_time),
                                # AURORA stop
    ( 37.4*mi,   38.0*mi, 55*mi/h, False, dwell_time),
    ( 38.0*mi,   39.0*mi, 35*mi/h, False, dwell_time),
    ( 39.0*mi,   40.0*mi, 75*mi/h, True, dwell_time),
                                # MONTGOMERY stop
    ( 40.0*mi,   43.3*mi, 79*mi/h, True, dwell_time),
                                # OSWEGO stop
                                # decently north of downtown Oswego
    ( 43.3*mi,   48.5*mi, 79*mi/h, True, dwell_time),
                                # YORKVILLE stop
                                # decently north of downtown Yorkville
    ( 48.5*mi,   52.7*mi, 79*mi/h, True, dwell_time),
                                # PLANO stop
                                # at Little Rock Rd, not in downtown Plano
    ( 52.7*mi,   56.9*mi, 79*mi/h, True, dwell_time),
                                # SANDWICH stop
                                # at Fairwind Blvd, not in downtown Sandwich
]

stops = {
    0.0*mi: 'Chicago Union Station',
    1.8*mi: 'Halsted St',
    3.7*mi: 'Western Ave',
    6.9*mi: 'Cicero',
    9.0*mi: 'LaVergne',
    9.5*mi: 'Berwyn',
    10.1*mi: 'Harlem Ave',
    11.0*mi: 'Riverside',
    11.8*mi: 'Hollywood',
    12.4*mi: 'Brookfield',
    13.0*mi: 'Congress Park',
    13.7*mi: 'LaGrange Rd',
    14.0*mi: 'Stone Ave',
    15.4*mi: 'Western Springs',
    16.3*mi: 'Highlands',
    16.8*mi: 'Hinsdale',
    17.7*mi: 'West Hinsdale',
    18.2*mi: 'Clarendon Hills',
    19.5*mi: 'Westmont',
    20.3*mi: 'Fairview Ave.',
    21.1*mi: 'Downers Grove',
    22.8*mi: 'Belmont',
    24.4*mi: 'Lisle',
    28.4*mi: 'Naperville',
    31.7*mi: 'Route 59',
    37.4*mi: 'Aurora',
    40.0*mi: 'Montgomery',
    43.3*mi: 'Oswego',
    48.5*mi: 'Yorkville',
    52.7*mi: 'Plano',
    56.9*mi: 'Sandwich'
}

dwell_time = 30 # seconds
