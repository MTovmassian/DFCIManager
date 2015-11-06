# -*- coding: utf-8 -*-
# python

"""
The module supplies a class to write status in a log file
"""

import time

class RecordStatusInLogfile(object):

	def __init__(self, logfile):
		self.logfile = logfile

	def limit_logfile_size(self):
		with open(self.logfile, "r") as lf:
			linescount = sum(1 for line in lf)
		if linescount > 1000:
			del_lines = ''.join(open(self.logfile, "r").readlines()[linescount-1000:linescount])
			with open(self.logfile, "w") as lf:
				lf.write(del_lines)
		else:
			None

	def record_status_in_logfile(self, status, status_sent_from_file):
		record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		with open(self.logfile, 'a') as lf:
			lf.write(record_time + " " + "\\" + status_sent_from_file + " -- " + status + '\n')
		self.limit_logfile_size()