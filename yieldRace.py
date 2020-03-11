'''
Created on 27 Mar 2019

@author: ostlerr
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter


rawdata = pd.read_csv('D:/code/python/workspace/LTEDataVis/src/data/bbkyields1968.csv',dtype={'year':int, 'plot':str, 'grain':float, 'colour':str})
years = rawdata['year'].unique()
plt.rcdefaults()
fig, ax = plt.subplots()

writer = FFMpegFileWriter()
writer.setup(fig, "test6.mp4", 100)

def init():
    pass

def update(i):
    year = years[i]
    yeardata = rawdata[rawdata['year'] == year].sort_values(by='grain',ascending=False)

    print(yeardata)
    
    ypos = np.arange(len(yeardata['treatment']))
    ax.barh(ypos, yeardata['grain'], align='center', color=yeardata['colour'], ecolor='black')
    #ax.set_xlabel(yeardata['treatment'])
    i = 0
    for idx, row in yeardata.iterrows():
        print(idx)
        plt.text(y = i+0.15, x=row['grain']-0.75, s = row['treatment'], size = 6)
        #plt.bar(i, height=row['grain'], color=row['colour'])
        i+=1
    
    ax.set_yticks(ypos)
    ax.set_yticklabels(yeardata['treatment'])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Yield')
    ax.set_title('Broadbalk yield race?')
#    writer.grab_frame()
#    return im

anim = FuncAnimation(fig, update, init_func=init, frames=len(years), interval=200, repeat=False)
fig.tight_layout()
plt.show()    
writer.finish()
