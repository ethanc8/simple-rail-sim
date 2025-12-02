scenario_name = "UP-N + KRM, limited-stop, 90 mph"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmupn.html and https://chicagorailfan.com/rfttucn.html
# Stations north of Kenosha are from satellite imagery
# Speed limits are from OpenRailwayMap

route = [
                                # OGILVIE stop
    (  0.0*mi,    0.2*mi, 30*mi/h, False, dwell_time),
    (  0.2*mi,    0.5*mi, 30*mi/h, False, dwell_time),
    (  0.5*mi,    2.8*mi, 50*mi/h, False, dwell_time),
                                # CLYBOURN stop
    (  2.8*mi,    3.5*mi, 50*mi/h, False, dwell_time),
    (  3.5*mi,    4.0*mi, 50*mi/h, False, dwell_time),
    (  4.0*mi,   12.0*mi, 90*mi/h, True, dwell_time),
                                # EVANSTON stop
    ( 12.0*mi,   16.6*mi, 90*mi/h, True, dwell_time),
                                # WINNETKA stop
    ( 16.6*mi,   19.2*mi, 90*mi/h, True, dwell_time),
                                # GLENCOE stop
    ( 19.2*mi,   23.0*mi, 90*mi/h, True, dwell_time),
                                # HIGHLAND PARK stop
    ( 23.0*mi,   28.3*mi, 90*mi/h, True, dwell_time),
                                # LAKE FOREST stop
    ( 28.3*mi,   35.9*mi, 90*mi/h, True, dwell_time),
                                # WAUKEGAN stop
    ( 35.9*mi,   51.6*mi, 90*mi/h, True, dwell_time),
                                # KENOSHA stop
    ( 51.6*mi,   61.7*mi, 90*mi/h, True, dwell_time),
                                # RACINE stop
    ( 61.7*mi,   83.0*mi, 90*mi/h, False, dwell_time),
    ( 83.0*mi,   84.2*mi, 30*mi/h, True, dwell_time),
                                # MILWAUKEE INTERMODAL stop

]

stops = {
    0.0:  'Chicago - Ogilvie',
    2.8:  'Clybourn',
    6.5:  'Ravenswood',
    8.1:  'Peterson/Ridge',
    9.4:  'Rogers Park',
    11.0*mi: 'Main Street',
    12.0*mi: 'Evanston',
    13.3*mi: 'Central Street',
    14.4*mi: 'Wilmette',
    15.2*mi: 'Kenilworth',
    15.8*mi: 'Indian Hill',
    16.6*mi: 'Winnetka',
    17.7*mi: 'Hubbard Woods',
    19.2*mi: 'Glencoe',
    20.5*mi: 'Braeside',
    20.9*mi: 'Ravinia Park',
    21.5*mi: 'Ravinia',
    23.0*mi: 'Highland Park',
    24.5*mi: 'Highwood',
    25.7*mi: 'Fort Sheridan',
    28.3*mi: 'Lake Forest',
    30.2*mi: 'Lake Bluff',
    32.2*mi: 'Great Lakes',
    33.7*mi: 'North Chicago',
    35.9*mi: 'Waukegan',
    42.1*mi: 'Zion',
    44.5*mi: 'Winthrop Harbor',
    51.6*mi: 'Kenosha',
    55.3*mi: 'Somers',
    61.7*mi: 'Racine',
    65.9*mi: 'Caledonia',
    72.0*mi: 'Oak Creek',
    74.7*mi: 'South Milwaukee',
    78.2*mi: 'Cudahy',
    81.5*mi: 'Lincoln Ave',
    84.2*mi: 'Milwaukee Intermodal'
}

dwell_time = 30 # seconds
