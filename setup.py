# -*- coding: utf-8 -*-
# python

try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

import DFCIManager, subprocess

setup(

	name = 'DFCIManager',

	version=DFCIManager.__version__,

	packages = find_packages(),

	author = "Martin Tovmassian",

	author_email = "martin.tovmassian@gmail.com",

	description = "Update data in a DFCI database running with PostGIS",

	long_description = open('README.md').read(),

	include_package_data = True,

    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Operating System :: Windows",
        "Programming Language :: Python :: 2.7",
        "Topic :: GIS",
    ]

)

subprocess.call("pip install psycopg2", shell=True)
subprocess.call("xcopy C:\Python27\Lib\site-packages\DFCIManager-0.0.1-py2.7.egg\DFCIManager\DFCIManager.lnk %AllUsersProfile%\desktop", shell=True)