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
    (  2.00*mi,    1.00*mi, 60*mi/h, True, dwell_time),
                                # MP 1.0 stop
    (  1.00*mi,    0.00*mi, 40*mi/h, True, dwell_time),
                                # MP 0.0 stop
]

stops = {
     0.00*mi: 'Station at MP 0.0',
     1.00*mi: 'Station at MP 1.0',
     2.00*mi: 'Station at MP 2.0',
}
