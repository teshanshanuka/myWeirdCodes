# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:04:49 2017

@author: Teshan Shanuka J
"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt

filepath  = "data set 3.log"
try:
    data = pd.read_csv(filepath , names=['DD','tt', 'TC', 'RTD', 'RT'])
except OSError:
    print("File Not Found")


total_time = (datetime.datetime.strptime(data.tt.iloc[-1], '%H:%M:%S') - \
                datetime.datetime.strptime(data.tt.iloc[0], '%H:%M:%S')).total_seconds()
timestep = total_time/(len(data)-1)

elapsed_times = []
for i in range(len(data)):
    elapsed_times.append(timestep*i)
    
data['et'] = pd.Series(elapsed_times)

fig = plt.figure()
plt.grid()
plt.title(filepath + ' Data')
plt.xlabel('Elapsed Time $(s)$')
plt.ylabel('TC Temperature $(^{\circ}C)$')

#plt.plot(data.et.values, data.TC.values, label = 'TC')
#
#### rolling mean
#
data['rm_TC_5'] = data.TC.rolling(window=5).mean()
data['rm_TC_10'] = data.TC.rolling(window=10).mean()
plt.plot(data.et.values, data['TC'].values, label = 'raw data')
plt.plot(data.et.values, data['rm_TC_5'].values, label = 'rm: window-5')
plt.plot(data.et.values, data['rm_TC_10'].values, label = 'rm: window-10')

#
plt.legend(fontsize =5)
plt.savefig(filepath.replace('.log','.pdf'), dpi=fig.dpi)