# -*- coding: utf-8 -*-
# python

import os, getpass, ConfigParser

"""
The module executes functions to get configuration parameters in a terminal prompt
and  write it in a configuration file.
"""

cfgfile = "C:\\Python27\\Lib\\site-packages\\DFCIManager-0.0.1-py2.7.egg\\DFCIManager\\dfcimanager.cfg"
config = ConfigParser.ConfigParser()

if os.path.exists(cfgfile) == True:
	os.remove(cfgfile)

new_cfgfile = open(cfgfile, 'a+')

config.add_section('Section1')

print "Directory path to save the DFCIManager logfile?"
logfile = raw_input('> ')
create_a_logfile = open(logfile + "\\DFCIManager.log", 'a+').close()
config.set('Section1','logfile', logfile + "\\DFCIManager.log")

print "DFCI PostGIS database host?"
host = raw_input('> ')
config.set('Section1','host', host)

print "DFCI PostGIS database port?"
port = raw_input('> ')
config.set('Section1','port', port)

print "DFCI PostGIS database name?"
dbname = raw_input('> ')
config.set('Section1','dbname', dbname)

print "DFCI PostGIS database user?"
user = raw_input('> ')
config.set('Section1','user',user)

print "DFCI PostGIS database password?"
password = getpass.getpass()
config.set('Section1','password', password)

config.write(new_cfgfile)
new_cfgfile.close()

exit(0)