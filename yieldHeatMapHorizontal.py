import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation,FFMpegFileWriter

rawdata = pd.read_csv('D:/code/python/workspace/LTEDataVis/src/data/bbkyields1968.csv',dtype={'year':int, 'plot':str, 'grain':float})
years = rawdata['year'].unique()
rawdata = rawdata.set_index(['year','plot'])

meandata = rawdata.groupby(level=['year','plot'])[['grain']].mean()

nulldata = meandata.transform(lambda x: x*0)
nulldata = nulldata.reset_index()
meandata = meandata.reset_index()
pivotdata = meandata.pivot(index='plot',columns='year',values='grain')
pivotnulldata = nulldata.pivot(index='plot',columns='year',values='grain')

pivotdata = pivotdata.reset_index()

fig = plt.figure(figsize=[12,6])

plt.title("Heatmap for grain yields from Broadbalk continuous wheat plots (section 9) 1968-2018")
ax = plt.axes()

plots = [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,3,22,21]
treatments = ['N1+N1+N1 KMg','N1+N2+N1 PKMg','N1+N4+N1 PKMg','N6 PKMg','N5 PKMg','N4 PKMg*','N4 PK','N1+N3+N1 PKMg','N4 PMg','N4','N4 PKMg','N3 PKMg','N2 PKMg','N1 PKMg','PKMg','Nil','FYM','FYM N2']
ax.set_yticks(np.arange(18))
ax.set_xticks(np.arange(51))
plt.xticks(fontsize=8)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

#ax.xaxis.set_ticks(np.arange(51))
ax.set_yticklabels(treatments)
ax.set_xticklabels(years)

data = np.random.rand(18,51)
newData = np.zeros((18,51))
i=0
while i <=50:
    year = years[i]
    k=0
    for j in ['19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','3','22','21']:
        d = pivotdata[pivotdata['plot'] == j]
        data[k,i] = d[year]
        k+=1
    i+=1
        
im = plt.imshow(data, aspect='auto')
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("tonnes/ha", rotation=-90, va="bottom")
def init():
    im.set_data(newData)

writer = FFMpegFileWriter()
writer.setup(fig, "test5.mp4", 600)
def update(i):
    year = years[i]
    k=0
    for j in ['19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','3','22','21']:
        d = pivotdata[pivotdata['plot'] == j]
        newData[k,i] = d[year]
        k+=1
    im.set_data(newData)
    writer.grab_frame()
    return im

ani = FuncAnimation(fig, update, init_func=init, frames=len(years), interval=200, repeat=False)
fig.tight_layout()
plt.show()    
writer.finish()