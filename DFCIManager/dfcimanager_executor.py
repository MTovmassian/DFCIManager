# -*- coding: utf-8 -*-
# python


"""
	The module supplies functions with different settings to run SQL queries
	in various ways in a PostGIS database.
"""

import config, sql_queries, pg_query

def run_update_queries_all(connection_parameters):
	try:
		for query_id, query_formula in sorted(sql_queries.sql_dict.items(), key = lambda (v1,v2) : (v2[0], v1)):
			query_to_pg = pg_query.QueryThePGDatabase(connection_parameters)
			query_to_pg.query_to_update_data(query_id, query_formula[1])
		status = ":) Mise à jour globale réussie!"
		return status
	except Exception:
		status = ":( Mise à jour impossible, consultez les logs"
		return status


def run_update_queries_by_tablename(connection_parameters, tablename):
	try:
		for query_id, query_formula in sorted(sql_queries.sql_dict.items(), key = lambda (v1,v2) : (v2[0], v1)):
			if query_id.split('.')[0] == tablename:
				query_to_pg = pg_query.QueryThePGDatabase(connection_parameters)
				query_to_pg.query_to_update_data(query_id, query_formula[1])
		status= ":) Mise à jour de la table %s réussie!" % tablename
		return status
	except Exception:
		status = ":( Mise à jour impossible, consultez les logs"
		return status


def get_data(connection_parameters, fieldname, tablename):
	connection_to_pg = pg_query.MakeAConnectionToPG(connection_parameters)
	query_to_pg = pg_query.QueryThePGDatabase(connection_to_pg)
	query = "select %s from %s" % (fieldname, tablename)
	data_list = query_to_pg.query_to_get_and_store_data('toto', query)
	return data_list

if __name__ == "__main__":
	connection_parameters = [config.host, config.port, config.dbname, config.user, config.password]
	run_update_queries_all(connection_parameters)