from units import *

scenario_name = "Metra Electric [current] - South Chicago Local [Main stations only]"

timetable_padding = 1.07
dwell_time = 30
long_dwell = 60

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmelec.html

route = [
    (  0.00*mi,    0.80*mi, 65*mi/h, True, dwell_time),
                                # VAN BUREN STREET stop
    (  0.80*mi,    1.43*mi, 65*mi/h, True, dwell_time),
                                # MUSEUM CAMPUS/11TH STREET stop
    (  1.43*mi,    2.22*mi, 65*mi/h, True, dwell_time),
                                # 18TH STREET stop
    (  2.22*mi,    2.68*mi, 65*mi/h, True, dwell_time),
                                # MCCORMICK PLACE/23RD STREET stop
    (  2.68*mi,    3.20*mi, 65*mi/h, True, dwell_time),
                                # 27TH STREET stop
    (  3.20*mi,    5.90*mi, 65*mi/h, True, dwell_time),
                                # 47TH STREET stop
    (  5.90*mi,    6.54*mi, 65*mi/h, True, dwell_time),
                                # 53RD STREET stop
    (  6.54*mi,    6.99*mi, 65*mi/h, True, dwell_time),
                                # 57TH STREET stop
    (  6.99*mi,    7.43*mi, 65*mi/h, True, dwell_time),
                                # 59TH STREET stop
    (  7.43*mi,    7.92*mi, 65*mi/h, True, dwell_time),
                                # 63RD STREET stop
    (  7.92*mi,    8.83*mi, 65*mi/h, True, dwell_time),
                                # [to SC]
]

stops = {
     0.00*mi: 'Randolph Street/Millennium Park',
     0.80*mi: 'Van Buren Street',
     1.43*mi: 'Museum Campus/11th Street',
     2.22*mi: '18th Street',
     2.68*mi: 'McCormick Place/23rd Street',
     3.20*mi: '27th Street',
    #  3.74*mi: '31st Street',
    #  4.82*mi: '39th Street',
     5.90*mi: '47th Street',
     6.54*mi: '53rd Street',
     6.99*mi: '57th Street',
     7.43*mi: '59th Street',
     7.92*mi: '63rd Street',
     8.33*mi: '67th Street',
     8.83*mi: '[to SC]',
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
    15.93*mi: '[to SSL]',
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

