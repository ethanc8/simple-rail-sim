scenario_name = "BNSF Line - express to zone 4, high-level boarding"

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
    (  3.7*mi,   21.1*mi, 70*mi/h, True, dwell_time),
                                # skip the rest of zones 2 and 3
                                # DOWNERS GROVE stop
    ( 21.1*mi,   22.8*mi, 70*mi/h, True, dwell_time),
                                # BELMONT stop
    ( 22.8*mi,   24.4*mi, 70*mi/h, True, dwell_time),
                                # LISLE stop
    ( 24.4*mi,   28.4*mi, 70*mi/h, True, dwell_time),
                                # NAPERVILLE stop
    ( 28.4*mi,   31.7*mi, 70*mi/h, True, dwell_time),
                                # ROUTE 59 stop
    ( 31.7*mi,   35.4*mi, 70*mi/h, False, dwell_time),
    ( 35.4*mi,   37.4*mi, 55*mi/h, True, dwell_time),
                                # AURORA stop
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
    37.4*mi: 'Aurora'
}

dwell_time = 30 # seconds
