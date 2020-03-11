import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter

rawdata = pd.read_csv('D:/code/python/workspace/LTEDataVis/src/data/bbkyields1968.csv',dtype={'year':int, 'plot':str, 'grain':float})
years = rawdata['year'].unique()
rawdata = rawdata.set_index(['year','plot'])

meandata = rawdata.groupby(level=['year','plot'])[['grain']].mean()

nulldata = meandata.transform(lambda x: x*0)
nulldata = nulldata.reset_index()
meandata = meandata.reset_index()
pivotdata = meandata.pivot(index='year',columns='plot',values='grain')
pivotnulldata = nulldata.pivot(index='year',columns='plot',values='grain')

pivotdata = pivotdata.reset_index()

fig = plt.figure()
ax = plt.axes()
plots = [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,3,22,21]
treatments = ['N1+N1+N1 KMg','N1+N2+N1 PKMg','N1+N4+N1 PKMg','N6 PKMg','N5 PKMg','N4 PKMg*','N4 PK','N1+N3+N1 PKMg','N4 PMg','N4','N4 PKMg','N3 PKMg','N2 PKMg','N1 PKMg','PKMg','Nil','FYM','FYM N2']
#ax.set_xticks(np.arange(18))
#ax.set_yticks(np.arange(51))
#ax.set_xticklabels(treatments)
#ax.set_yticklabels(years)

plt.yticks(np.arange(0.5, 51, 1),years)
plt.xticks(np.arange(0.5, 18, 1),treatments)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

data = np.random.rand(51,18)
newData = np.zeros((51,18))
i=0
while i <=50:
    d = pivotdata[pivotdata['year'] == years[i]]
    k=0
    #for j in ['N1+N1+N1 KMg','N1+N2+N1 PKMg','N1+N4+N1 PKMg','N6 PKMg','N5 PKMg','N4 PKMg*','N4 PK','N1+N3+N1 PKMg','N4 PMg','N4','N4 PKMg','N3 PKMg','N2 PKMg','N1 PKMg','PKMg','Nil','FYM','FYM N2']:
    for j in ['19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','3','22','21']:
        data[i,k] = d[j]
        k+=1
    i+=1
        
im = plt.imshow(data)
def init():
    im.set_data(newData)

writer = FFMpegFileWriter()
writer.setup(fig, "test5.mp4", 100)
def update(i):
    year = years[i]
    d = pivotdata[pivotdata['year'] == year]
    print(d)
    k=0
    
    for j in ['19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','3','22','21']:
        newData[i,k] = d[j]
        #text = ax.text(k, i, newData[i, k],ha="center", va="center", color="w")
        k+=1
    im.set_data(newData)
    writer.grab_frame()
    #print(newData)
    return im

ani = FuncAnimation(fig, update, init_func=init, frames=len(years), interval=200, repeat=False)
plt.show()    
writer.finish()
#ani.save('climate_spiral.gif', dpi=120, writer='imagemagick', savefig_kwargs={'facecolor': '#323331'})

#print(newData)
#fig = plt.figure()
#im = plt.imshow(newData)
#plt.show()


