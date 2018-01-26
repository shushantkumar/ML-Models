import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data') 	#data downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
df.replace('?',-99999, inplace=True)				#replacing unknown dataset with large negative value

X = np.array(df.drop(['class'], 1))					#from dataset dropping column class which is the column to be predicted
y = np.array(df['class'])							#the column to be predicted

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)	#Splitting dataset into training and test set

clf = neighbors.KNeighborsClassifier()				#Applying KNeighborsClassifier to training data
clf.fit(X_train, y_train)			
accuracy = clf.score(X_test, y_test)				#score returns the accuracy of the trained data
print(accuracy)