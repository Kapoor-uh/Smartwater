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

def GetWeightedRainfallAndFlow(cursor, pump, window, n_windows):
	flow = None
	weighted_rainfall = None
	for i in range(0, n_windows):
		cursor = pumpData.getRainfallPumpingOutput(cursor, pump, 0, 24, -window * (i + 1), -window * i, 4,10)
		response = cursor.fetchall()
		response = map(list, zip(*response))
		flow = np.array(response[1])
		rainfall = np.array(response[2])
		weighted_rainfall = rainfall if i == 0 else weighted_rainfall + rainfall / (2 ** i)
	return flow, weighted_rainfall

while rainfall_window <= 4 * 7 * 24:
	for pump in pumps[0:20]:
		flow, rainfall = GetWeightedRainfallAndFlow(cursor, pump, rainfall_window, 4)
		threshold = np.percentile(flow, flow_filter_percentile)
		flow_rainfall = zip(*np.array(zip(flow, rainfall))[np.less_equal(flow, threshold)])
		correlation = np.corrcoef(*flow_rainfall)[0, 1]
		print(pump, "window h: ", rainfall_window, "correlation ", round(correlation, 3))
		plotter.save_figure_pump_rain(*flow_rainfall, name=str(rainfall_window) + "h-" + pump, folder='plots')
	rainfall_window *= 2
