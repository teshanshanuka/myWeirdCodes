import pandas as pd
import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm

filepath  = "Test 13/5.05k serires resistance 2.log"
try:
    data = pd.read_csv(filepath , names=['DD','tt', 'RTD', 'TC', 'RT'])
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
plt.xlabel('Elapsed Time $(s)$')
plt.ylabel('Temperature')

#plt.plot(data.et.values, data.RTD.values, label = 'RTD')
#plt.plot(data.et.values, data.TC.values, label = 'TC')
#plt.plot(data.et.values, data.RT.values, label = 'RT')

### rolling mean

data['rm_TC'] = data.TC.rolling(window=5).mean()
plt.plot(data.et.values, data.TC.values, label = 'raw data')
plt.plot(data.et.values, data.rm_TC.values, label = 'rolling mean')

### rolling median

data['rmd_TC'] = data.TC.rolling(window=5).median()
plt.plot(data.et.values, data.rmd_TC.values, label = 'rolling median')

### ordinary least sqyare regression for trend line
regr = sm.OLS(data.TC.values, sm.add_constant(data.et.values))
fitted = regr.fit()
plt.plot(data.et.values, fitted.fittedvalues, label = 'OLS fitted line')

data['OLS_TC'] = pd.Series(fitted.fittedvalues)


#print(fitted.summary())
RMSE_raw = ((data.OLS_TC - data.TC)**2).mean()**.5
print('RMSE_raw : %.3f'% RMSE_raw)
RMSE_rm = ((data.OLS_TC - data.rm_TC)**2).mean()**.5
print('RMSE_rm_TC : %.3f'% RMSE_rm)
RMSE_rmd = ((data.OLS_TC - data.rmd_TC)**2).mean()**.5
print('RMSE_rmd_TC : %.3f'% RMSE_rmd)


plt.legend()
#plt.savefig('new.pdf', dpi=fig.dpi)