scenario_name = "Metra Electric - Blue Island Branch, express"

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
    (  2.22,   6.99, mph(65), True),
                                # 57TH STREET stop
    (  6.99,  14.49, mph(65), True),
                                # 115TH-KENSINGTON stop
    ( 14.49,  15.60, mph(65), True),
                                # STATE STREET stop
    ( 15.60,  16.06, mph(30), True),
                                # STEWART RIDGE stop
    ( 16.06,  16.68, mph(30), True),
                                # WEST PULLMAN stop
    ( 16.68,  17.04, mph(30), True),
                                # RACINE AVENUE stop
    ( 17.04,  17.87, mph(30), True),
                                # ASHLAND AVENUE stop
    ( 17.87,  18.36, mph(30), True),
                                # BURR OAK stop
    ( 18.36,  18.91, mph(30), True),
                                # BLUE ISLAND stop
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
    15.60: 'State Street',
    16.06: 'Stewart Ridge',
    16.68: 'West Pullman',
    17.04: 'Racine Avenue',
    17.87: 'Ashland Avenue',
    18.36: 'Burr Oak',
    18.91: 'Blue Island',
}

dwell_time = 30 # seconds
