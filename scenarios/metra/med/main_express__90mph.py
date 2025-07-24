scenario_name = "Metra Electric - Main Line, express (90mph)"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 65mph speed limit

route = [
    (  0.00,   0.80, mph(90), True),
                                # VAN BUREN STREET stop
    (  0.80,   1.43, mph(90), True),
                                # MUSEUM CAMPUS/11TH STREET stop
    (  1.43,   2.22, mph(90), True),
                                # 18TH STREET stop
    (  2.22,   6.99, mph(90), True),
                                # 57TH STREET stop
    (  6.99,  14.49, mph(90), True),
                                # 115TH-KENSINGTON stop
    ( 14.49,  17.33, mph(90), True),
                                # RIVERDALE stop
    ( 17.33,  18.18, mph(90), True),
                                # IVANHOE stop
    ( 18.18,  18.98, mph(90), True),
                                # 147TH STREET stop
    ( 18.98,  20.00, mph(90), True),
                                # HARVEY stop
    ( 20.00,  22.27, mph(90), True),
                                # HAZEL CREST stop
    ( 22.27,  22.82, mph(90), True),
                                # CALUMET stop
    ( 22.82,  23.51, mph(90), True),
                                # HOMEWOOD stop
    ( 23.51,  24.93, mph(90), True),
                                # FLOSSMOOR stop
    ( 24.93,  26.56, mph(90), True),
                                # OLYMPIA FIELDS stop
    ( 26.56,  27.62, mph(90), True),
                                # 211TH STREET stop
    ( 27.62,  28.24, mph(90), True),
                                # MATTESON stop
    ( 28.24,  29.33, mph(90), True),
                                # RICHTON PARK stop
    ( 29.33,  31.50, mph(90), True),
                                # UNIVERSITY PARK stop
]

stops = {
     0.00: 'Randolph Street/Millennium Park',
     0.80: 'Van Buren Street',
     1.43: 'Museum Campus/11th Street',
     2.22: '18th Street',
     2.68: 'McCormick Place/23rd Street',
     3.20: '27th Street',
     5.90: '47th Street',
     6.54: '53rd Street',
     6.99: '57th Street',
     7.43: '59th Street',
     7.92: '63rd Street',
     8.33: '67th Street',
     9.32: '75th-Grand Crossing',
     9.99: '79th-Chatham',
    10.38: '83rd-Avalon Park',
    10.86: '87th-Woodruff',
    11.37: '91st-Chesterfield',
    12.04: '95th-Chicago State University',
    13.06: '103rd Street',
    13.54: '107th Street',
    13.95: '111th-Pullman',
    14.49: '115th-Kensington',
    17.33: 'Riverdale',
    18.18: 'Ivanhoe',
    18.98: '147th Street',
    20.00: 'Harvey',
    22.27: 'Hazel Crest',
    22.82: 'Calumet',
    23.51: 'Homewood',
    24.93: 'Flossmoor',
    26.56: 'Olympia Fields',
    27.62: '211th Street',
    28.24: 'Matteson',
    29.33: 'Richton Park',
    31.50: 'University Park',
}

dwell_time = 30 # seconds
