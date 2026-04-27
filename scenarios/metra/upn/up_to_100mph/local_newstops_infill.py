from units import *

scenario_name = "UP-N locals"

timetable_padding = 1.07
dwell_time = 30
long_dwell = 60

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts from https://www.chicagorailfan.com/mmupn.html
# Some KRM mileposts from satellite imagery -- TODO: Figure out all the station locations
# Speed limits from https://docs.google.com/spreadsheets/d/1lPyNgtQ9q6uX23JEhGTpyvfEQdKdjVL2ZDsLBIVREmQ/edit?gid=797601041#gid=797601041

route = [
    # Ogilvie to Northwest Jct is part of Geneva Sub
                                # OGILVIE stop
    (  0.0*mi,    0.3*mi, 10*mi/h, False, dwell_time),
    (  0.3*mi,    0.5*mi, 15*mi/h, False, dwell_time),
    # Northwest Jct at MP 0.5
    # Northwest Jct to Clybourn is part of Harvard Sub
    (  0.5*mi,    1.0*mi, 35*mi/h, True, dwell_time),
                                # CHICAGO AVE stop
    (  1.0*mi,    2.2*mi, 35*mi/h, True, dwell_time),
                                # NORTH AVE stop
    (  2.2*mi,    2.8*mi, 35*mi/h, True, dwell_time),
                                # CLYBOURN stop
    (  2.8*mi,    3.5*mi, 100*mi/h, True, dwell_time),
                                # FULLERTON AVE stop
    (  3.5*mi,    4.5*mi, 100*mi/h, False, dwell_time),
                                # BELMONT AVE stop
    (  4.5*mi,    5.5*mi, 100*mi/h, False, dwell_time),
                                # IRVING PARK RD stop
    (  5.5*mi,    6.5*mi, 100*mi/h, True, dwell_time),
                                # RAVENSWOOD stop
    (  6.5*mi,    8.1*mi, 100*mi/h, True, dwell_time),
                                # PETERSON/RIDGE stop
    (  8.1*mi,    9.4*mi, 100*mi/h, True, dwell_time),
                                # ROGERS PARK stop
    (  9.4*mi,   11.0*mi, 100*mi/h, True, dwell_time),
                                # MAIN STREET stop
    ( 11.0*mi,   12.0*mi, 100*mi/h, True, dwell_time),
                                # EVANSTON stop
    ( 12.0*mi,   13.3*mi, 100*mi/h, True, dwell_time),
                                # CENTRAL STREET stop
    ( 13.3*mi,   14.4*mi, 100*mi/h, True, dwell_time),
                                # WILMETTE stop
    ( 14.4*mi,   15.2*mi, 100*mi/h, True, dwell_time),
                                # KENILWORTH stop
    ( 15.2*mi,   15.8*mi, 100*mi/h, True, dwell_time),
                                # INDIAN HILL stop
    ( 15.8*mi,   16.6*mi, 100*mi/h, True, dwell_time),
                                # WINNETKA stop
    ( 16.6*mi,   17.7*mi, 100*mi/h, True, dwell_time),
                                # HUBBARD WOODS stop
    ( 17.7*mi,   19.2*mi, 100*mi/h, True, dwell_time),
                                # GLENCOE stop
    ( 19.2*mi,   20.5*mi, 100*mi/h, True, dwell_time),
                                # BRAESIDE stop
    ( 20.5*mi,   20.9*mi, 100*mi/h, True, long_dwell), # Due to events letting out
                                # RAVINIA PARK stop
    ( 20.9*mi,   21.5*mi, 100*mi/h, True, dwell_time),
                                # RAVINIA stop
    ( 21.5*mi,   23.0*mi, 100*mi/h, True, dwell_time),
                                # HIGHLAND PARK stop
    ( 23.0*mi,   24.5*mi, 100*mi/h, True, dwell_time),
                                # HIGHWOOD stop
    ( 24.5*mi,   25.7*mi, 100*mi/h, True, dwell_time),
                                # FT. SHERIDAN stop
    ( 25.7*mi,   28.3*mi, 100*mi/h, True, dwell_time),
                                # LAKE FOREST stop
    ( 28.3*mi,   30.2*mi, 100*mi/h, True, dwell_time),
                                # LAKE BLUFF stop
    ( 30.2*mi,   32.2*mi, 100*mi/h, True, dwell_time),
                                # GREAT LAKES stop
    ( 32.2*mi,   33.7*mi, 100*mi/h, True, dwell_time),
                                # NORTH CHICAGO stop
    ( 33.7*mi,   35.9*mi, 100*mi/h, True, dwell_time),
                                # WAUKEGAN stop
    ( 35.9*mi,   36.1*mi,  93*mi/h, False, dwell_time),
                                # Waukegan 10th St curve
    ( 36.1*mi,   42.1*mi, 100*mi/h, True, dwell_time),
                                # ZION stop
    ( 42.1*mi,   44.5*mi, 100*mi/h, True, dwell_time),
                                # WINTHROP HARBOR stop
    ( 44.5*mi,   51.6*mi, 100*mi/h, True, dwell_time),
                                # KENOSHA stop
    ( 51.6*mi,   53.5*mi, 100*mi/h, False, dwell_time),
    ( 53.5*mi,   54.0*mi,  80*mi/h, True, dwell_time),
                                # CARTHAGE COLLEGE stop
    ( 54.0*mi,   54.2*mi,  80*mi/h, False, dwell_time),
                                # Kenosha 19th St curve
    ( 54.2*mi,   57.4*mi, 100*mi/h, True, dwell_time),
                                # HWY 195 stop
    ( 57.4*mi,   59.6*mi, 100*mi/h, False, dwell_time),
    ( 59.6*mi,   59.7*mi,  98*mi/h, False, dwell_time),
                                # Racine Gillen St curve
                                # FIXME: The Racine Jct curve (60.4~60.6) cannot be simulated
                                # because the train has to decelerate enough before reaching
                                # the curve.
    ( 59.7*mi,   60.8*mi, 100*mi/h, True, dwell_time),
                                # UPTOWN RACINE stop
    ( 60.8*mi,   61.7*mi, 100*mi/h, True, dwell_time),
                                # RACINE stop
    ( 61.7*mi,   62.0*mi,  61*mi/h, False, dwell_time),
                                # Racine State St curve
    ( 62.0*mi,   65.9*mi, 100*mi/h, True, dwell_time),
                                # CALEDONIA stop
    ( 65.9*mi,   72.0*mi, 100*mi/h, True, dwell_time),
                                # CARROLLVILLE stop
    ( 72.0*mi,   74.7*mi, 100*mi/h, True, dwell_time),
                                # SOUTH MILWAUKEE stop
    ( 74.7*mi,   76.1*mi, 100*mi/h, True, dwell_time),
                                # COLLEGE AVE stop
    ( 76.1*mi,   77.7*mi, 100*mi/h, False, dwell_time),
    # MP 77.7~78.2 - Library Dr curve
    ( 77.7*mi,   78.2*mi,  78*mi/h, True, dwell_time),
                                # CUDAHY stop
    ( 78.2*mi,   79.6*mi, 100*mi/h, False, dwell_time),
    ( 79.6*mi,   79.9*mi,  50*mi/h, True, dwell_time),
                                # ST FRANCIS stop
                                # St Francis Ave overpass
                                # very tight around this area
    # St. Francis (79.9) - end of Kenosha Sub
    #                      beginning of National Ave Industrial Lead
    #                      This industrial lead is kinda curvy due to the 
    #                      expressway taking up part of the ROW
    ( 79.9*mi,   81.0*mi,  50*mi/h, True, dwell_time),
                                # BAY VIEW stop
    ( 81.0*mi,   83.0*mi,  50*mi/h, True, dwell_time),
                                # NATIONAL AVE stop
    # MP 83.0 - switch from National Ave Industrial Lead to MILW (CPKC, approach to Milwaukee Intermodal)
    ( 83.0*mi,   84.2*mi,  30*mi/h, True, dwell_time),
                                # MILWAUKEE INTERMODAL stop
]

stops = {
    0.0*mi:  'Chicago - Ogilvie',
    1.0*mi:  'Chicago Ave',
    2.2*mi:  'North Ave',
    2.8*mi:  'Clybourn',
    3.5*mi:  'Fullerton Ave',
    4.5*mi:  'Belmont Ave',
    5.5*mi:  'Irving Park Rd',
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
    54.0*mi: 'Carthage College',
    57.4*mi: 'Hwy 195',
    60.8*mi: 'Uptown Racine',
    61.7*mi: 'Racine',
    65.9*mi: 'Caledonia',
    72.0*mi: 'Carrollville',
    74.7*mi: 'South Milwaukee',
    76.1*mi: 'College Ave',
    78.2*mi: 'Cudahy',
    79.9*mi: 'St Francis',
    81.0*mi: 'Bay View',
    83.0*mi: 'National Ave',
    84.2*mi: 'Milwaukee Intermodal'
}

dwell_time = 60 # seconds
