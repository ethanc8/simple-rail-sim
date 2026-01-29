# express_offset = 12.5 * 60

# Based on the December 2025 schedule, 4pm to 5pm outbound
# https://schedules.metrarail.com/pdf/ME.pdf
# https://mysouthshoreline.com/wp-content/uploads/2025/06/SSL.061025.A.JulyTimetablePDFs-D1.pdf
trips = [
  ('metra.med.current.bi_local_main', 'highliner_ii', 0 * 60, 'Blue Island Local', 'tab:blue'),
  ('metra.med.current.ssl_main', 'highliner_ii', 4 * 60, 'South Shore Line', 'tab:red'),
  ('metra.med.current.homewood_express', 'highliner_ii', 8 * 60, 'Homewood Express', 'tab:green'),
  ('metra.med.current.sc_local_main', 'highliner_ii', 11 * 60, 'Kensington Express', 'tab:grey'),
  ('metra.med.current.ssl_main', 'highliner_ii', 22 * 60, 'South Shore Line', 'tab:red'),
  ('metra.med.current.sc_local_main', 'highliner_ii', 25 * 60, 'South Chicago Local', 'tab:grey'),
  ('metra.med.current.bi_local_main', 'highliner_ii', 26 * 60, 'Blue Island Local', 'tab:blue'),
  ('metra.med.current.homewood_express', 'highliner_ii', 32 * 60, 'Homewood Express', 'tab:green'),
  ('metra.med.current.sc_local_main', 'highliner_ii', 40 * 60, 'Kensington Express', 'tab:grey'),
  ('metra.med.current.sc_local_main', 'highliner_ii', 45 * 60, 'South Chicago Local', 'tab:grey'),
  ('metra.med.current.homewood_express', 'highliner_ii', 55 * 60, 'Homewood Express', 'tab:green'),
  ('metra.med.current.ssl_main', 'highliner_ii', 60 * 60, 'South Shore Line', 'tab:red'),
]

name = "ME Stringline"
