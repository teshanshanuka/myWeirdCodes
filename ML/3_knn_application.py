# dataset: http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('bcdata.txt')
df.replace('?', -99999, inplace=True)
# id is not useful
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[3,1,2,1,2,3,1,1,1],[5,1,3,1,2,2,2,1,1]])
# reshape to avoid stupid warning
prediction = clf.predict(example_measures.reshape(2,-1))

print(prediction)
