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
flow_filter_percentile = 90

for rainfall_window in [4,8,16,24,48,96,128]
	for pump in pumps[0:40]:
    rainfall_window_start = rainfall_window/4
		cursor = pumpData.getRainfallPumpingOutput(cursor, pump, 0, 24, -rainfall_window, -rainfall_window_start,4,10)
		response = cursor.fetchall()
    response = map(list, zip(*response))
    flow = np.array(response[1])
    rainfall = np.array(response[2])
    threshold = np.percentile(flow, flow_filter_percentile)
    flow_rainfall = zip(*np.array(zip(flow, rainfall))[np.less_equal(flow, threshold)])
    correlation = np.corrcoef(*flow_rainfall)[0, 1]
    print(response[0][0], "window h: ", rainfall_window, "correlation ", round(correlation, 3))
	plotter.save_figure_pump_rain(flow,rainfall, name=str(rainfall_window) + "h-" + str(rainfall_window_start) + "h-" + pump, folder='plots')
