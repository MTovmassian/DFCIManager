# -*- coding: utf-8 -*-
# python

import ConfigParser

"""
The module executes functions to retrieve configuration parameters
"""

config = ConfigParser.ConfigParser()
config.read("dfcimanager.cfg")

logfile = config.get("Section1", "logfile")

host = config.get("Section1", "host")

port = config.get("Section1", "port")

dbname = config.get("Section1", "dbname")

user = config.get("Section1", "user")

password = config.get("Section1", "password")