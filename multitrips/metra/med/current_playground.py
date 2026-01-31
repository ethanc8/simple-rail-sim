from units import *
express_offset = 12.5 * minute

trips = []

for i in range(8):
  start = i * 15*minute
  trips.extend([
    ('metra.med.current.homewood_local', 'highliner_ii', start + 0*minute, 'Homewood Local', 'tab:blue'),
    ('metra.med.current.ssl_main', 'highliner_ii', start + 5*minute + 20*s, 'South Shore Line', 'tab:red'),
    ('metra.med.current.sc_local_main', 'highliner_ii', start + 8*minute, 'South Chicago Local', 'tab:purple'),
    ('metra.med.current.homewood_express_nd', 'highliner_ii', start + 13*minute + 20*s, 'Homewood Express', 'tab:green'),
])
  

name = "ME Stringline"
