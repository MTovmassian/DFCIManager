DFCIManager
===============================================================================
This package allows to automaticly update fields in the tables of the
PostGIS DFCI database.

Setup steps
-------------------------------------------------------------------------------
1. Create a PostGIS database and import the various DFCI shapefiles
(especially tro.shp, deb.shp and eau.shp).

2. Download the latest stable version of Python27 for Windows at
https://www.python.org/downloads/windows/ and install it in the
*C:\\* directory.

3. After Python27 installation, make sure the *C:\\Python27\\* and the
*C:\\Python27\\Scripts* directories have been added to the PATH environment variable.

4. Download the *DFCIManager-master.zip* file.

5. Enter the downloads directory and unzip the *DFCIManager-master.zip* file. Then enter
the new created *DFCIManager-master* directory and execute the *run*.*py* file inside.

6. A window shell is displayed and show the setup process. If the pip install psycopg2
command failed just download the .exe file at 
http://www.stickpeople.com/projects/python/win-psycopg/, install it manually and 
re-execute the *run*.*py* file. At the end of the setup process 6 configuration 
parameters are required. Fill them manually one after the other.

7. Launch the DFCIManager application by double clicking on the DFCIManager
shortcut placed on your desktop or on the one placed in the 
*C:\\Python27\\Lib\site-packages\\DFCIManager-0.0.1-py2.7.egg\\DFCIManager\\* directory.
