from units import *
express_offset = 12.5 * minute

trips = []

for i in range(4):
  start = i * 30*minute
  trips.extend([
    ('metra.med.current.bi_local_main', 'highliner_ii', start + 0*minute, 'Blue Island Local', 'tab:blue'),
    ('metra.med.current.homewood_express', 'highliner_ii', start + 5*minute + 20*s, 'Homewood Express', 'tab:green'),
    ('metra.med.current.sc_local_main', 'highliner_ii', start + 7.5*minute, 'South Chicago Local', 'tab:purple'),
    ('metra.med.current.ssl_main', 'highliner_ii', start + 7.5*minute + 5*minute + 20*s, 'South Shore Line', 'tab:red'),
    ('metra.med.current.bi_local_main', 'highliner_ii', start + 15*minute, 'Blue Island Local', 'tab:blue'),
    ('metra.med.current.kensington_express', 'highliner_ii', start + 20*minute + 20*s, 'Kensington Express', 'tab:olive'),
    ('metra.med.current.sc_local_main', 'highliner_ii', start + 23.5*minute, 'South Chicago Local', 'tab:purple'),
    ('metra.med.current.ssl_main', 'highliner_ii', start + 23.5*minute + 5*minute + 20*s, 'South Shore Line', 'tab:red'),
  ])
  

name = "ME Stringline"
