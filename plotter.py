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



