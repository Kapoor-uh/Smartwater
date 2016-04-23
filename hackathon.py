import os
import numpy as np
import matplotlib.pyplot as plt

def ensure_dir(f):
    c = os.getcwd()
    d = c+"\\"+f
    if not os.path.exists(d):
        os.makedirs(d)

def sava_figure_pump_rain(pump,rain,name,folder = None):
    fig = plt.figure()
    plt.plot(pump,rain,".")
    path = "" if folder==None else folder+"/"
    fig.savefig(path + name+".png")

a = np.arange(10)
b=a*a
folder = "folder"
ensure_dir(folder)
sava_figure_pump_rain(a,b,"pic",folder)


def load_pump_rain_data(file):
    rows = open(file)
    matrix = np.matrix([[float(number)for number in row.split(" ")] for row in rows[1:]])
    return matrix


def plot_1_pump_rain_data(pump, rain):
    plt.figure()

    plt.plot(pump,rain,".")
    plt.show()

def plot_n_pump_rain_data(pumps,rains):
    for pump,rain in zip(pumps,rains):
        plot_1_pump_rain_data(pump,rain)

def to_linear__pump_data(pumps):
    #return np.matrix([pumps,np.multiply(pumps,pumps),np.ones(len(pumps))]).T #squared
    return np.matrix([pumps,np.ones(len(pumps))]).T                           #linear

def to_linear_rain_data(rains):
    #return np.matrix([rains,np.multiply(rains,rains),np.ones(len(rains))]).T  #squared
    return np.matrix([rains,np.ones(len(rains))]).T                           #linear

def linear_correlation(pump,rain):
    return np.corrcoef(pump,rain)

def linear_correlations(pumps,rains):
    return np.matrix([[linear_correlation(pump,rain)] for pump,rain in zip(pumps,rains)])





