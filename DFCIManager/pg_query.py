# -*- coding: utf-8 -*-
# python

import psycopg2, os, log, config

"""
	The module supplies 2 classes to make a connection with a PostGIS
	database and execute a SQL query.
"""

class MakeAConnectionToPG(object):

	def __init__(self, connection_parameters, logfile):		
		self.connection_parameters = connection_parameters
		self.conn_set = "host=%s port=%s dbname=%s user=%s password=%s" \
		% (self.connection_parameters[0], self.connection_parameters[1], \
			self.connection_parameters[2], self.connection_parameters[3], self.connection_parameters[4])

		self.logfile = logfile
		self.log = log.RecordStatusInLogfile(self.logfile)

	def open_connection_to_pg(self, query_id):
		try:
			conn = psycopg2.connect(self.conn_set)
			conn.autocommit = True
			status = "[%s] => Connection successful to the %s database" % (query_id, self.connection_parameters[2])
			self.log.record_status_in_logfile(status, os.path.basename(__file__))
			pgcursor = conn.cursor()
			print status
			return pgcursor
		except Exception, error:
			status = str(error)
			self.log.record_status_in_logfile(status, os.path.basename(__file__))
			print status

	def close_connection_to_pg(self, current_pgcursor):
		pgcursor = current_pgcursor
		pgcursor.close()
		print "closed connection"	

class QueryThePGDatabase(object):

	def __init__(self, connection_parameters):

		logfile = config.logfile
		self.log = log.RecordStatusInLogfile(logfile)

		self.connection_to_pg = MakeAConnectionToPG(connection_parameters, logfile)

	def execute_query_in_pg(self, query_id, query_formula):
		try:
			pgcursor = self.connection_to_pg.open_connection_to_pg(query_id)
			pgcursor.execute(query_formula)
			status = "[%s] => Query successful" % (query_id)
			self.log.record_status_in_logfile(status, os.path.basename(__file__))
			print status
			return pgcursor
		except Exception, error:
			status = "[%s] => [%s]" % (query_id, str(error))
			self.log.record_status_in_logfile(status, os.path.basename(__file__))
			print status

	def query_to_update_data(self, query_id, query_formula):
		pgcursor = self.execute_query_in_pg(query_id, query_formula)
		self.connection_to_pg.close_connection_to_pg(pgcursor)

	def query_to_get_and_show_data(self, query_id, query_formula):
		pgcursor = self.execute_query_in_pg(query_id, query_formula)
		rows = pgcursor.fetchall()
		for row in rows:
			print row[0]
		self.connection_to_pg.close_connection_to_pg(pgcursor)

	def query_to_get_and_store_data(self, query_id, query_formula):
		pgcursor = self.execute_query_in_pg(query_id, query_formula)
		rows = pgcursor.fetchall()
		data_list = []
		for values in rows:
			for value in values:
				data_list.append(value)
		return data_list
		self.connection_to_pg.close_connection_to_pg(pgcursor)