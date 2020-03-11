'''
Created on 6 Jun 2019

@author: https://github.com/sebastianbeyer/warmingstripes
'''
import numpy as np
import matplotlib.pyplot as plt

## get data from file
## this one is from dwd, and edited a little to be read with numpy
## ftp://ftp-cdc.dwd.de/pub/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt
data = np.loadtxt("D:/code/python/workspace/LTEDataVis/src/data/RothTemps.txt", skiprows=1)
temps = data[:,1]

## stack data to be able to plot them with imshow
#temps = temps_germany
# temps = temps_bremen
# temps = temps_berlin_brandenburg




stacked_temps = np.stack((temps, temps))

vmin = 5.9
vmax = 11
## plotting
###############
plt.figure(figsize=(4,18))
# img = plt.imshow(stacked_temps, cmap='RdBu_r', aspect=40, vmin=vmin, vmax=vmax)
img = plt.imshow(stacked_temps, cmap='RdBu_r', aspect=40, )

plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig("stripes.png", bbox_inches = 'tight',
    pad_inches = 0, dpi=400)