scenario_name = "UP-N - current locals, high-level boarding"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupnw.html
# Speed limits are from OpenRailwayMap

route = [
                                # OGILVIE stop
    (  0.0,   0.2, mph(10), False),
    (  0.2,   0.5, mph(15), False),
    (  0.5,   2.8, mph(35), True),
                                # CLYBOURN stop
    (  2.8,   3.5, mph(35), False),
    (  3.5,   7.6, mph(110), True),
                                # MAYFAIR stop
    (  7.6,   9.7, mph(110), True),
                                # GLADSTONE PARK stop
    (  9.7,  11.1, mph(110), True),
                                # NORWOOD PARK stop
    ( 11.1,  12.3, mph(110), True),
                                # EDISON PARK stop
    ( 12.3,  13.1, mph(110), True),
                                # PARK RIDGE stop
    ( 13.1,  14.7, mph(110), True),
                                # DEE ROAD stop
    ( 14.7,  16.7, mph(110), True),
                                # DES PLAINES stop
    ( 16.7,  18.2, mph(110), True),
                                # CUMBERLAND stop
    ( 18.2,  19.6, mph(110), True),
                                # MT. PROSPECT stop
    ( 19.6,  22.5, mph(110), True),
                                # ARLINGTON HEIGHTS stop
    ( 22.5,  24.2, mph(110), True),
                                # ARLINGTON PARK stop
    ( 24.2,  26.4, mph(110), True),
                                # PALATINE stop
    ( 26.4,  31.5, mph(110), True),
                                # BARRINGTON stop
    ( 31.5,  37.0, mph(70), True),
                                # FOX RIVER GROVE stop
    ( 37.0,  38.3, mph(70), True),
                                # CARY stop
    ( 38.3,  41.8, mph(70), True),
                                # PINGREE ROAD stop
    ( 41.8,  42.9, mph(70), True),
                                # CRYSTAL LAKE stop
    ( 42.9,  45.7, mph(70), True),
                                # RIDGEFIELD stop
    ( 45.7,  51.3, mph(70), True),
                                # WOODSTOCK stop
    ( 51.3,  55.7, mph(70), True),
                                # HARTLAND stop
    ( 55.7,  62.8, mph(70), True),
                                # HARVARD stop
]

stops = {
    0.0:  'Chicago - Ogilvie',
    2.8:  'Clybourn',
    7.6:  'Mayfair',
    9.7:  'Gladstone Park',
    11.1: 'Norwood Park',
    12.3: 'Edison Park',
    13.1: 'Park Ridge',
    14.7: 'Dee Road',
    16.7: 'Des Plaines',
    18.2: 'Cumberland',
    19.6: 'Mt. Prospect',
    22.5: 'Arlington Heights',
    24.2: 'Arlington Park',
    26.4: 'Palatine',
    31.5: 'Barrington',
    37.0: 'Fox River Grove',
    38.3: 'Cary',
    41.8: 'Pingree Road',
    42.9: 'Crystal Lake',
    45.7: 'Ridgefield',
    51.3: 'Woodstock',
    55.7: 'Hartland',
    62.8: 'Harvard',
}

dwell_time = 30 # seconds
