scenario_name = "Metra Electric - Blue Island Branch"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 65mph speed limit

route = [
    (  0.00,   0.80, mph(15), True),
                                # VAN BUREN STREET stop
    (  0.80,   1.43, mph(20), True),
                                # MUSEUM CAMPUS/11TH STREET stop
    (  1.43,   2.22, mph(50), True),
                                # 18TH STREET stop
    (  2.22,   2.68, mph(65), True),
                                # MCCORMICK PLACE/23RD STREET stop
    (  2.68,   3.20, mph(65), True),
                                # 27TH STREET stop
    (  3.20,   5.90, mph(65), True),
                                # 47TH STREET stop
    (  5.90,   6.54, mph(65), True),
                                # 53RD STREET stop
    (  6.54,   6.99, mph(65), True),
                                # 57TH STREET stop
    (  6.99,   7.43, mph(65), True),
                                # 59TH STREET stop
    (  7.43,   7.92, mph(65), True),
                                # 63RD STREET stop
    (  7.92,   8.33, mph(65), True),
                                # 67TH STREET stop
    ( 8.33,  9.10, mph(15), True),
                                # STONY ISLAND AVENUE stop
    ( 9.10,  9.66, mph(30), True),
                                # BRYN MAWR stop
    ( 9.66, 10.28, mph(30), True),
                                # SOUTH SHORE stop
    (10.28, 10.88, mph(30), True),
                                # 75TH-WINDSOR PARK stop
    (10.88, 11.49, mph(30), True),
                                # 79TH-CHELTENHAM stop
    (11.49, 11.97, mph(30), True),
                                # 83RD STREET stop
    (11.97, 12.51, mph(30), True),
                                # 87TH STREET stop
    (12.51, 13.04, mph(30), True),
                                # 93RD-SOUTH CHICAGO stop
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
     9.10: 'Stony Island Avenue',
     9.66: 'Bryn Mawr',
    10.28: 'South Shore',
    10.88: '75th-Windsor Park',
    11.49: '79th-Cheltenham',
    11.97: '83rd Street',
    12.51: '87th Street',
    13.04: '93rd-South Chicago',
}

dwell_time = 30 # seconds
