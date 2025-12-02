scenario_name = "Metra Electric - Main Line, express (90mph)"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 65mph speed limit

route = [
    (  0.00*mi,    0.80*mi, 15*mi/h, True, dwell_time),
                                # VAN BUREN STREET stop
    (  0.80*mi,    1.43*mi, 20*mi/h, True, dwell_time),
                                # MUSEUM CAMPUS/11TH STREET stop
    (  1.43*mi,    2.22*mi, 50*mi/h, True, dwell_time),
                                # 18TH STREET stop
    (  2.22*mi,    6.99*mi, 65*mi/h, True, dwell_time),
                                # 57TH STREET stop
    (  6.99*mi,   14.49*mi, 65*mi/h, True, dwell_time),
                                # 115TH-KENSINGTON stop
    ( 14.49*mi,   17.33*mi, 65*mi/h, True, dwell_time),
                                # RIVERDALE stop
    ( 17.33*mi,   18.18*mi, 65*mi/h, True, dwell_time),
                                # IVANHOE stop
    ( 18.18*mi,   18.98*mi, 65*mi/h, True, dwell_time),
                                # 147TH STREET stop
    ( 18.98*mi,   20.00*mi, 65*mi/h, True, dwell_time),
                                # HARVEY stop
    ( 20.00*mi,   22.27*mi, 65*mi/h, True, dwell_time),
                                # HAZEL CREST stop
    ( 22.27*mi,   22.82*mi, 65*mi/h, True, dwell_time),
                                # CALUMET stop
    ( 22.82*mi,   23.51*mi, 65*mi/h, True, dwell_time),
                                # HOMEWOOD stop
    ( 23.51*mi,   24.93*mi, 65*mi/h, True, dwell_time),
                                # FLOSSMOOR stop
    ( 24.93*mi,   26.56*mi, 65*mi/h, True, dwell_time),
                                # OLYMPIA FIELDS stop
    ( 26.56*mi,   27.62*mi, 65*mi/h, True, dwell_time),
                                # 211TH STREET stop
    ( 27.62*mi,   28.24*mi, 65*mi/h, True, dwell_time),
                                # MATTESON stop
    ( 28.24*mi,   29.33*mi, 65*mi/h, True, dwell_time),
                                # RICHTON PARK stop
    ( 29.33*mi,   31.50*mi, 65*mi/h, True, dwell_time),
                                # UNIVERSITY PARK stop
]

stops = {
     0.00*mi: 'Randolph Street/Millennium Park',
     0.80*mi: 'Van Buren Street',
     1.43*mi: 'Museum Campus/11th Street',
     2.22*mi: '18th Street',
     2.68*mi: 'McCormick Place/23rd Street',
     3.20*mi: '27th Street',
     5.90*mi: '47th Street',
     6.54*mi: '53rd Street',
     6.99*mi: '57th Street',
     7.43*mi: '59th Street',
     7.92*mi: '63rd Street',
     8.33*mi: '67th Street',
     9.32*mi: '75th-Grand Crossing',
     9.99*mi: '79th-Chatham',
    10.38*mi: '83rd-Avalon Park',
    10.86*mi: '87th-Woodruff',
    11.37*mi: '91st-Chesterfield',
    12.04*mi: '95th-Chicago State University',
    13.06*mi: '103rd Street',
    13.54*mi: '107th Street',
    13.95*mi: '111th-Pullman',
    14.49*mi: '115th-Kensington',
    17.33*mi: 'Riverdale',
    18.18*mi: 'Ivanhoe',
    18.98*mi: '147th Street',
    20.00*mi: 'Harvey',
    22.27*mi: 'Hazel Crest',
    22.82*mi: 'Calumet',
    23.51*mi: 'Homewood',
    24.93*mi: 'Flossmoor',
    26.56*mi: 'Olympia Fields',
    27.62*mi: '211th Street',
    28.24*mi: 'Matteson',
    29.33*mi: 'Richton Park',
    31.50*mi: 'University Park',
}

dwell_time = 30 # seconds
