scenario_name = "UP-N - current locals, high-level boarding"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupn.html
# Speed limits are from OpenRailwayMap

route = [
                                # OGILVIE stop
    (  0.0,   0.2, mph(10), False),
    (  0.2,   0.5, mph(15), False),
    (  0.5,   2.8, mph(35), True),
                                # CLYBOURN stop
    (  2.8,   3.5, mph(35), False),
    (  3.5,   4.0, mph(50), False),
    (  4.0,   6.5, mph(70), True),
                                # RAVENSWOOD stop
    (  6.5,   8.1, mph(70), True),
                                # PETERSON/RIDGE stop
    (  8.1,   9.4, mph(70), True),
                                # ROGERS PARK stop
    (  9.4,  11.0, mph(70), True),
                                # MAIN STREET stop
    ( 11.0,  12.0, mph(70), True),
                                # EVANSTON stop
    ( 12.0,  13.3, mph(70), True),
                                # CENTRAL STREET stop
    ( 13.3,  14.4, mph(70), True),
                                # WILMETTE stop
    ( 14.4,  15.2, mph(70), True),
                                # KENILWORTH stop
    ( 15.2,  15.8, mph(70), True),
                                # INDIAN HILL stop
    ( 15.8,  16.6, mph(70), True),
                                # WINNETKA stop
    ( 16.6,  17.7, mph(70), True),
                                # HUBBARD WOODS stop
    ( 17.7,  19.2, mph(70), True),
                                # GLENCOE stop
    ( 19.2,  20.5, mph(70), True),
                                # BRAESIDE stop
    ( 20.5,  20.9, mph(70), True),
                                # RAVINIA PARK stop
    ( 20.9,  21.5, mph(70), True),
                                # RAVINIA stop
    ( 21.5,  23.0, mph(70), True),
                                # HIGHLAND PARK stop
    ( 23.0,  24.5, mph(70), True),
                                # HIGHWOOD stop
    ( 24.5,  25.7, mph(70), True),
                                # FT. SHERIDAN stop
    ( 25.7,  28.3, mph(70), True),
                                # LAKE FOREST stop
    ( 28.3,  30.2, mph(70), True),
                                # LAKE BLUFF stop
    ( 30.2,  32.2, mph(70), True),
                                # GREAT LAKES stop
    ( 32.2,  33.7, mph(70), True),
                                # NORTH CHICAGO stop
    ( 33.7,  35.9, mph(70), True),
                                # WAUKEGAN stop
    ( 35.9,  42.1, mph(70), True),
                                # ZION stop
    ( 42.1,  44.5, mph(70), True),
                                # WINTHROP HARBOR stop
    ( 44.5,  51.6, mph(70), True),
                                # KENOSHA stop
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
}

dwell_time = 30 # seconds
