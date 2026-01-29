from units import *

dwell_time = 30 # seconds

timetable_padding = 1.07

scenario_name = "Metra Electric - Main Line"

# convert mph to km/h
def mph(speed):
    return speed * 1.609344

# Each tuple: (start, end, speed limit (m/s), ends at stop, dwell time)

# Mileposts are from https://chicagorailfan.com/mmelec.html
# Assume 65mph speed limit

route = [
    (  1.00*mi,    2.00*mi, 60*mi/h, True, dwell_time),
                                # STATION C stop
    (  2.00*mi,    3.00*mi, 40*mi/h, True, dwell_time),
                                # STATION D stop
]

stops = {
     0.00*mi: 'Station A',
     1.00*mi: 'Station B',
     2.00*mi: 'Station C',
     3.00*mi: 'Station D',
}
