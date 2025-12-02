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
    (  2.22*mi,    6.99*mi, 65*mi/h, True, dwell_time),
                                # 57TH STREET stop
    (  6.99*mi,    7.43*mi, 65*mi/h, True, dwell_time),
                                # 59TH STREET stop
    (  7.43*mi,    7.92*mi, 65*mi/h, False, dwell_time),
                                # 63RD STREET skip
    (  7.92*mi,    8.33*mi, 65*mi/h, False, dwell_time),
                                # 67TH STREET skip
    ( 8.33*mi,   9.10*mi, 15*mi/h, True, dwell_time),
                                # STONY ISLAND AVENUE stop
    ( 9.10*mi,   9.66*mi, 30*mi/h, True, dwell_time),
                                # BRYN MAWR stop
    ( 9.66*mi,  10.28*mi, 30*mi/h, True, dwell_time),
                                # SOUTH SHORE stop
    (10.28*mi,  10.88*mi, 30*mi/h, True, dwell_time),
                                # 75TH-WINDSOR PARK stop
    (10.88*mi,  11.49*mi, 30*mi/h, True, dwell_time),
                                # 79TH-CHELTENHAM stop
    (11.49*mi,  11.97*mi, 30*mi/h, True, dwell_time),
                                # 83RD STREET stop
    (11.97*mi,  12.51*mi, 30*mi/h, True, dwell_time),
                                # 87TH STREET stop
    (12.51*mi,  13.04*mi, 30*mi/h, True, dwell_time),
                                # 93RD-SOUTH CHICAGO stop
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
     9.10*mi: 'Stony Island Avenue',
     9.66*mi: 'Bryn Mawr',
    10.28*mi: 'South Shore',
    10.88*mi: '75th-Windsor Park',
    11.49*mi: '79th-Cheltenham',
    11.97*mi: '83rd Street',
    12.51*mi: '87th Street',
    13.04*mi: '93rd-South Chicago',
}

dwell_time = 30 # seconds
