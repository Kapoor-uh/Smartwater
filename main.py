#!/usr/bin/python
import numpy as np
import pyodbc
import plotter
import parsePumps
import pumpData

dsn = 'awr'
user = 'AWR_DEV'
password = 'NEO'
database = 'AWR'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)
cursor = cnxn.cursor()

rainfall_window = 1
pumps = parsePumps.ParseHighQualityPumps()
while rainfall_window <= 4 * 7 * 24:
	for pump in pumps[0:30]:
		cursor = pumpData.getRainfallPumpingOutput(cursor, pump, 0, 24, -rainfall_window, 0)
		response = cursor.fetchall()
		response = map(list, zip(*response))
		flow = response[1]
		rainfall = response[2]
		correlation = np.corrcoef(rainfall, flow)[0, 1]
		print(response[0][0], "window h: ", rainfall_window, "correlation ", round(correlation, 3))
		plotter.save_figure_pump_rain(flow, rainfall, pump + "-" + str(rainfall_window), 'plots')
	rainfall_window *= 2
