# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.datasets import make_moons, make_circles, make_classification
# from sklearn.neural_network import MLPClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.gaussian_process import GaussianProcessClassifier
# from sklearn.gaussian_process.kernels import RBF
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
#above versions can also be used

#a sequence to sequence encoder uses two rnn one encoder another decoder

from sklearn import tree
from sklearn import neural_network

clf = tree.DecisionTreeClassifier()
clf1= neural_network.MLPClassifier()


# [height, weight, some_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Train our data
clf = clf.fit(X, Y)
clf1 = clf1.fit(X,Y)

prediction = clf.predict([[190, 70, 35]])
prediction1 = clf.predict([[190, 70, 35]])
# CHALLENGE compare their reusults and print the best one!

print(prediction)
print(prediction1)