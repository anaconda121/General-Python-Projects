from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

"""
Basics Datset Stuff
	columns = features
	rows = sample data
	target-variable = dependent variable
"""
iris = datasets.load_iris()
"""
K-Nearest Neighbors - Classificiation Algorithm
	Algoritham that takes in an integer k and a test value. The algorithm relies upon 2 classes, which are
	generated from analysis of the dataset. The algorithm takes in the test value and places it in the 
	middle of the graph. Then, based on the number k, the algorithm will draw a circle around the test
	value until k amount of class reps are included in the circle. Next, the algorithm looks at the 
	reps and tallies the number from each class. Whichever class has a majority is the class that is
	classified to the test value.

	In other situations, the algorithm will split the graph into different parts, where each part is 
	associated to a certain class value

	Good Practices:
		k must always be an odd to prevent ties
"""

knn = KNeighborsClassifier(n_neighbors = 7) #sets k to 6

"""
Requirements for .fit()
	data as numpy array or panda dataframe
	columns in dataset must take on continous values, not constants that can't be changed
	data can't have no missing values
"""

knn.fit(iris['data'], iris['target']) #data = rows , target = columns, train model  

#using model
X_new = np.array([[5.6, 2.8, 3.9, 1.1], [5.7, 2.6, 3.8, 1.3], [4.7, 3.2, 1.3, 0.2]])
prediction = knn.predict(X_new)

height, width = X_new.shape
newPrediction = np.ones([height, width], dtype = "<U6")

for i in range (prediction.size):
	if(prediction[i] == 0):
		newPrediction[i] = 'setosa'
	elif(prediction[i] == 1):
		newPrediction[i] = 'versicolor'
	elif(prediction[i] == 2):
		newPrediction[i] == 'virginica'

print('Prediction: \n{}'.format(newPrediction)) #has to return 3 by 1 array because 
# 1 means versicolor, 0 means setosa, 2 means virginica
