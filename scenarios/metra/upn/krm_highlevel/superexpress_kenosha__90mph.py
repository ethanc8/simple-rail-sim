scenario_name = "KRM super-express to Kenosha, 90 mph"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupn.html and https://chicagorailfan.com/rfttucn.html
# Stations north of Kenosha are from satellite imagery
# Speed limits are from OpenRailwayMap

route = [
                                # OGILVIE stop
    (  0.0,   0.2, mph(30), False),
    (  0.2,   0.5, mph(30), False),
    (  0.5,   2.8, mph(50), False),
                                # skip CLYBOURN
    (  2.8,   3.5, mph(50), False),
    (  3.5,   4.0, mph(50), False),
    (  4.0,  35.9, mph(90), True),
                                # skip until Waukegan
                                # WAUKEGAN stop
    ( 35.9,  42.1, mph(90), False),
                                # skip ZION
    ( 42.1,  44.5, mph(90), False),
                                # skip WINTHROP HARBOR
    ( 44.5,  51.6, mph(90), True),
                                # KENOSHA stop
    ( 51.6,  55.3, mph(90), True),
                                # SOMERS stop
    ( 55.3,  61.7, mph(90), True),
                                # RACINE stop
    ( 61.7,  65.9, mph(90), True),
                                # CALEDONIA stop
    ( 65.9,  72.0, mph(90), True),
                                # OAK CREEK stop
    ( 72.0,  74.7, mph(90), True),
                                # SOUTH MILWAUKEE stop
    ( 74.7,  78.2, mph(90), True),
                                # CUDAHY stop
    ( 78.2,  81.5, mph(90), True),
                                # LINCOLN AVE stop
    ( 81.5,  83.0, mph(90), False),
    ( 83.0,  84.2, mph(30), True),
                                # MILWAUKEE INTERMODAL stop

]

stops = {
    0.0:  'Chicago - Ogilvie',
    2.8:  'Clybourn',
    6.5:  'Ravenswood',
    8.1:  'Peterson/Ridge',
    9.4:  'Rogers Park',
    11.0: 'Main Street',
    12.0: 'Evanston',
    13.3: 'Central Street',
    14.4: 'Wilmette',
    15.2: 'Kenilworth',
    15.8: 'Indian Hill',
    16.6: 'Winnetka',
    17.7: 'Hubbard Woods',
    19.2: 'Glencoe',
    20.5: 'Braeside',
    20.9: 'Ravinia Park',
    21.5: 'Ravinia',
    23.0: 'Highland Park',
    24.5: 'Highwood',
    25.7: 'Fort Sheridan',
    28.3: 'Lake Forest',
    30.2: 'Lake Bluff',
    32.2: 'Great Lakes',
    33.7: 'North Chicago',
    35.9: 'Waukegan',
    42.1: 'Zion',
    44.5: 'Winthrop Harbor',
    51.6: 'Kenosha',
    55.3: 'Somers',
    61.7: 'Racine',
    65.9: 'Caledonia',
    72.0: 'Oak Creek',
    74.7: 'South Milwaukee',
    78.2: 'Cudahy',
    81.5: 'Lincoln Ave',
    84.2: 'Milwaukee Intermodal'
}

dwell_time = 30 # seconds
