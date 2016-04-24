import os
import numpy as np
import matplotlib.pyplot as plt

def ensure_dir(f):
	c = os.getcwd()
	d = c+"\\"+f
	if not os.path.exists(d):
		os.makedirs(d)

def save_figure_pump_rain(pump,rain,name,folder = None):
	fig = plt.figure()
	plt.title(name)
	plt.xlabel("rain")
	plt.ylabel("pump")
	plt.plot(rain,pump,".")
	path = "" if folder==None else folder+"/"
	fig.savefig(path + name+".png")
	plt.close(fig)


def save_histogram_pump_rain(pump,rainn,name,folder = None):
	name = "histogram-" + name
	rain = []
	norain = []
	pumpval = 0
	for pumpval, rainval in zip(pump, rainn):
		if(rainval > 0.001):
			rain.append(pumpval)
		else:
			norain.append(pumpval)
	fig = plt.figure()	
	plt.title(name)
	maxVal = max(norain) if len(rain) == 0 else max(max(norain), max(rain))
	bins = np.arange(0, 20) / 20.0 * maxVal
	if len(norain) > 0:
		plt.hist(x=np.array(norain), bins=bins, alpha=0.5, normed = 1, label='dry')
	if len(rain) > 0:
		plt.hist(x=np.array(rain), bins=bins, alpha=0.5, normed = 1, label='rain')
	path = "" if folder==None else folder+"/"
	fig.savefig(path + name+".png")
	plt.close(fig)
