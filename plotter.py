import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

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
	text = "{} dry days: {} rainy days: {} p-value: {}".format(name, len(norain), len(rain), calculateP(p=0.5, dry=norain, wet=rain))
	plt.title(text)
	maxVal = max(norain) if len(rain) == 0 else max(max(norain), max(rain))
	bins = np.arange(0, 20) / 20.0 * maxVal
	if len(norain) > 0:
		plt.hist(x=np.array(norain), bins=bins, alpha=0.5, normed = 1, label='dry', color='brown')
	if len(rain) > 0:
		plt.hist(x=np.array(rain), bins=bins, alpha=0.5, normed = 1, label='rain', color='blue')
	path = "" if folder==None else folder+"/"
	fig.savefig(path + name+".png")
	plt.close(fig)


def calculateP(p, dry, wet):
	p = 0.5
	threshold = np.median(dry)
	wetHigh = 0
	wetLow = 0
	for wetVal in wet:
		if wetVal > threshold:
			wetHigh += 1
		else:
			wetLow += 1
	if(wetHigh + wetLow == 0):
		return 0.5
	pValue = 1 - (0 if wetHigh == 0 else st.binom.cdf(wetHigh - 1, wetHigh + wetLow, p))
	pValue = round(pValue, 3)
	text = "Above mean: {} Below mean: {} p-value: {}".format(wetHigh, wetLow, pValue)
	print(text)
	return pValue




