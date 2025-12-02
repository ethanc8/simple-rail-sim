scenario_name = "Metra Electric - Blue Island Branch"

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
    (  7.92*mi,    8.33*mi, 65*mi/h, True, dwell_time),
                                # 67TH STREET stop
    (  8.33*mi,    9.32*mi, 65*mi/h, True, dwell_time),
                                # 75TH-GRAND CROSSING stop
    (  9.32*mi,    9.99*mi, 65*mi/h, True, dwell_time),
                                # 79TH-CHATHAM stop
    (  9.99*mi,   10.38*mi, 65*mi/h, True, dwell_time),
                                # 83RD-AVALON PARK stop
    ( 10.38*mi,   10.86*mi, 65*mi/h, True, dwell_time),
                                # 87TH-WOODRUFF stop
    ( 10.86*mi,   11.37*mi, 65*mi/h, True, dwell_time),
                                # 91ST-CHESTERFIELD stop
    ( 11.37*mi,   12.04*mi, 65*mi/h, True, dwell_time),
                                # 95TH-CHICAGO STATE UNIVERSITY stop
    ( 12.04*mi,   13.06*mi, 65*mi/h, True, dwell_time),
                                # 103RD STREET stop
    ( 13.06*mi,   13.54*mi, 65*mi/h, True, dwell_time),
                                # 107TH STREET stop
    ( 13.54*mi,   13.95*mi, 65*mi/h, True, dwell_time),
                                # 111TH-PULLMAN stop
    ( 13.95*mi,   14.49*mi, 65*mi/h, True, dwell_time),
                                # 115TH-KENSINGTON stop
    ( 14.49*mi,   15.60*mi, 65*mi/h, True, dwell_time),
                                # STATE STREET stop
    ( 15.60*mi,   16.06*mi, 30*mi/h, True, dwell_time),
                                # STEWART RIDGE stop
    ( 16.06*mi,   16.68*mi, 30*mi/h, True, dwell_time),
                                # WEST PULLMAN stop
    ( 16.68*mi,   17.04*mi, 30*mi/h, True, dwell_time),
                                # RACINE AVENUE stop
    ( 17.04*mi,   17.87*mi, 30*mi/h, True, dwell_time),
                                # ASHLAND AVENUE stop
    ( 17.87*mi,   18.36*mi, 30*mi/h, True, dwell_time),
                                # BURR OAK stop
    ( 18.36*mi,   18.91*mi, 30*mi/h, True, dwell_time),
                                # BLUE ISLAND stop
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
    15.60*mi: 'State Street',
    16.06*mi: 'Stewart Ridge',
    16.68*mi: 'West Pullman',
    17.04*mi: 'Racine Avenue',
    17.87*mi: 'Ashland Avenue',
    18.36*mi: 'Burr Oak',
    18.91*mi: 'Blue Island',
}

dwell_time = 30 # seconds
