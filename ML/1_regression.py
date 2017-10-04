# https://youtu.be/JcI5Vnw0b2c?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

# another tutorial
# http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

import pandas as pd
import numpy as np
import quandl, math, datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# High-low percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close']* 100.0

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open']* 100.0

#           price        x             x              x
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# we want to forecast the price
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# predict for number of dates size of some percentage of the dataset
forecast_out = math.ceil(0.1*len(df))

df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'],1))
# # scale(): Standardize a dataset along any axis
# # Center to the mean and component wise scale to unit variance.
X = preprocessing.scale(x)

X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])
y_lately = y[-forecast_out:]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# classifier
# use support vector regression
# clf = svm.SVR() # (kernel='poly')

# use linear regression
clf = LinearRegression()

# train the classifier
clf.fit(X_train, y_train)
# # save the trained classifier
# with open('lin_reg.pickle','wb') as f:
#     pickle.dump(clf, f)
#
# # load the saved classifier
# pickle_in = open('lin_reg.pickle', 'rb')
# clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)

# print(forecast_set, accuracy, forecast_out)
print("accuracy : ", accuracy)

df['Forecast'] = np.nan
df['Actual'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix+one_day

for i, j in zip(forecast_set, y_lately):
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-2)] +[i] + [j]

df['Adj. Close'].plot()
df['Forecast'].plot()
df['Actual'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
