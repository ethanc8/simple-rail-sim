scenario_name = "UP-N - current locals, high-level boarding"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmupnw.html
# Speed limits are from OpenRailwayMap

route = [
                                # OGILVIE stop
    (  0.0*mi,    0.2*mi, 10*mi/h, False, dwell_time),
    (  0.2*mi,    0.5*mi, 15*mi/h, False, dwell_time),
    (  0.5*mi,    2.8*mi, 35*mi/h, True, dwell_time),
                                # CLYBOURN stop
    (  2.8*mi,    3.5*mi, 35*mi/h, False, dwell_time),
    (  3.5*mi,    7.6*mi, 110*mi/h, True, dwell_time),
                                # MAYFAIR stop
    (  7.6*mi,    9.7*mi, 110*mi/h, False, dwell_time),
                                # GLADSTONE PARK stop
    (  9.7*mi,   11.1*mi, 110*mi/h, False, dwell_time),
                                # NORWOOD PARK stop
    ( 11.1*mi,   12.3*mi, 110*mi/h, False, dwell_time),
                                # EDISON PARK stop
    ( 12.3*mi,   13.1*mi, 110*mi/h, False, dwell_time),
                                # PARK RIDGE stop
    ( 13.1*mi,   14.7*mi, 110*mi/h, False, dwell_time),
                                # DEE ROAD stop
    ( 14.7*mi,   16.7*mi, 110*mi/h, True, dwell_time),
                                # DES PLAINES stop
    ( 16.7*mi,   18.2*mi, 110*mi/h, True, dwell_time),
                                # CUMBERLAND stop
    ( 18.2*mi,   19.6*mi, 110*mi/h, True, dwell_time),
                                # MT. PROSPECT stop
    ( 19.6*mi,   22.5*mi, 110*mi/h, True, dwell_time),
                                # ARLINGTON HEIGHTS stop
    ( 22.5*mi,   24.2*mi, 110*mi/h, True, dwell_time),
                                # ARLINGTON PARK stop
    ( 24.2*mi,   26.4*mi, 110*mi/h, True, dwell_time),
                                # PALATINE stop
    ( 26.4*mi,   31.5*mi, 110*mi/h, True, dwell_time),
                                # BARRINGTON stop
    ( 31.5*mi,   37.0*mi, 70*mi/h, True, dwell_time),
                                # FOX RIVER GROVE stop
    ( 37.0*mi,   38.3*mi, 70*mi/h, True, dwell_time),
                                # CARY stop
    ( 38.3*mi,   41.8*mi, 70*mi/h, True, dwell_time),
                                # PINGREE ROAD stop
    ( 41.8*mi,   42.9*mi, 70*mi/h, True, dwell_time),
                                # CRYSTAL LAKE stop
    ( 42.9*mi,   45.7*mi, 70*mi/h, True, dwell_time),
                                # RIDGEFIELD stop
    ( 45.7*mi,   51.3*mi, 70*mi/h, True, dwell_time),
                                # WOODSTOCK stop
    ( 51.3*mi,   55.7*mi, 70*mi/h, True, dwell_time),
                                # HARTLAND stop
    ( 55.7*mi,   62.8*mi, 70*mi/h, True, dwell_time),
                                # HARVARD stop
]

stops = {
    0.0:  'Chicago - Ogilvie',
    2.8:  'Clybourn',
    7.6:  'Mayfair',
    9.7:  'Gladstone Park',
    11.1*mi: 'Norwood Park',
    12.3*mi: 'Edison Park',
    13.1*mi: 'Park Ridge',
    14.7*mi: 'Dee Road',
    16.7*mi: 'Des Plaines',
    18.2*mi: 'Cumberland',
    19.6*mi: 'Mt. Prospect',
    22.5*mi: 'Arlington Heights',
    24.2*mi: 'Arlington Park',
    26.4*mi: 'Palatine',
    31.5*mi: 'Barrington',
    37.0*mi: 'Fox River Grove',
    38.3*mi: 'Cary',
    41.8*mi: 'Pingree Road',
    42.9*mi: 'Crystal Lake',
    45.7*mi: 'Ridgefield',
    51.3*mi: 'Woodstock',
    55.7*mi: 'Hartland',
    62.8*mi: 'Harvard',
}

dwell_time = 30 # seconds
