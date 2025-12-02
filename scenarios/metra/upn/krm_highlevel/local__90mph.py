from units import *

dwell_time = 30 # seconds

timetable_padding = 1.07

scenario_name = "UP-N + KRM, high-level boarding, 90mph"

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
    (  0.5*mi,    2.8*mi, 50*mi/h, True, dwell_time),
                                # CLYBOURN stop
    (  2.8*mi,    3.5*mi, 50*mi/h, False, dwell_time),
    (  3.5*mi,    4.0*mi, 50*mi/h, False, dwell_time),
    (  4.0*mi,    6.5*mi, 90*mi/h, True, dwell_time),
                                # RAVENSWOOD stop
    (  6.5*mi,    8.1*mi, 90*mi/h, True, dwell_time),
                                # PETERSON/RIDGE stop
    (  8.1*mi,    9.4*mi, 90*mi/h, True, dwell_time),
                                # ROGERS PARK stop
    (  9.4*mi,   11.0*mi, 90*mi/h, True, dwell_time),
                                # MAIN STREET stop
    ( 11.0*mi,   12.0*mi, 90*mi/h, True, dwell_time),
                                # EVANSTON stop
    ( 12.0*mi,   13.3*mi, 90*mi/h, True, dwell_time),
                                # CENTRAL STREET stop
    ( 13.3*mi,   14.4*mi, 90*mi/h, True, dwell_time),
                                # WILMETTE stop
    ( 14.4*mi,   15.2*mi, 90*mi/h, True, dwell_time),
                                # KENILWORTH stop
    ( 15.2*mi,   15.8*mi, 90*mi/h, True, dwell_time),
                                # INDIAN HILL stop
    ( 15.8*mi,   16.6*mi, 90*mi/h, True, dwell_time),
                                # WINNETKA stop
    ( 16.6*mi,   17.7*mi, 90*mi/h, True, dwell_time),
                                # HUBBARD WOODS stop
    ( 17.7*mi,   19.2*mi, 90*mi/h, True, dwell_time),
                                # GLENCOE stop
    ( 19.2*mi,   20.5*mi, 90*mi/h, True, dwell_time),
                                # BRAESIDE stop
    ( 20.5*mi,   20.9*mi, 90*mi/h, True, dwell_time),
                                # RAVINIA PARK stop
    ( 20.9*mi,   21.5*mi, 90*mi/h, True, dwell_time),
                                # RAVINIA stop
    ( 21.5*mi,   23.0*mi, 90*mi/h, True, dwell_time),
                                # HIGHLAND PARK stop
    ( 23.0*mi,   24.5*mi, 90*mi/h, True, dwell_time),
                                # HIGHWOOD stop
    ( 24.5*mi,   25.7*mi, 90*mi/h, True, dwell_time),
                                # FT. SHERIDAN stop
    ( 25.7*mi,   28.3*mi, 90*mi/h, True, dwell_time),
                                # LAKE FOREST stop
    ( 28.3*mi,   30.2*mi, 90*mi/h, True, dwell_time),
                                # LAKE BLUFF stop
    ( 30.2*mi,   32.2*mi, 90*mi/h, True, dwell_time),
                                # GREAT LAKES stop
    ( 32.2*mi,   33.7*mi, 90*mi/h, True, dwell_time),
                                # NORTH CHICAGO stop
    ( 33.7*mi,   35.9*mi, 90*mi/h, True, dwell_time),
                                # WAUKEGAN stop
    ( 35.9*mi,   42.1*mi, 90*mi/h, True, dwell_time),
                                # ZION stop
    ( 42.1*mi,   44.5*mi, 90*mi/h, True, dwell_time),
                                # WINTHROP HARBOR stop
    ( 44.5*mi,   51.6*mi, 90*mi/h, True, dwell_time),
                                # KENOSHA stop
    ( 51.6*mi,   55.3*mi, 90*mi/h, True, dwell_time),
                                # SOMERS stop
    ( 55.3*mi,   61.7*mi, 90*mi/h, True, dwell_time),
                                # RACINE stop
    ( 61.7*mi,   65.9*mi, 90*mi/h, True, dwell_time),
                                # CALEDONIA stop
    ( 65.9*mi,   72.0*mi, 90*mi/h, True, dwell_time),
                                # OAK CREEK stop
    ( 72.0*mi,   74.7*mi, 90*mi/h, True, dwell_time),
                                # SOUTH MILWAUKEE stop
    ( 74.7*mi,   78.2*mi, 90*mi/h, True, dwell_time),
                                # CUDAHY stop
    ( 78.2*mi,   81.5*mi, 90*mi/h, True, dwell_time),
                                # LINCOLN AVE stop
    ( 81.5*mi,   83.0*mi, 90*mi/h, False, dwell_time),
    ( 83.0*mi,   84.2*mi, 30*mi/h, True, dwell_time),
                                # MILWAUKEE INTERMODAL stop

]

stops = {
    0.0*mi:  'Chicago - Ogilvie',
    2.8*mi:  'Clybourn',
    6.5*mi:  'Ravenswood',
    8.1*mi:  'Peterson/Ridge',
    9.4*mi:  'Rogers Park',
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

