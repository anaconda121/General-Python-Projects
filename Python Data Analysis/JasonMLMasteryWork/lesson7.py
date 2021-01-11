# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:46:00 2020

@author: tanis
"""

#notes
""""
K-Fold Cross Validation - used to evalulate accuracy of machine learning algorithm
                        single parameter called k that refers to the number of groups that a given data sample is to be split into
                        
Steps
    Shuffle the dataset randomly.
    Split the dataset into k groups
    For each unique group:
        Take the group as a hold out or test data set
        Take the remaining groups as a training data set
        Fit a model on the training set and evaluate it on the test set
        Retain the evaluation score and discard the model
        Summarize the skill of the model using the sample of model evaluation scores

Logistic Regression - used to predict outcome given a set of variables, gives outcome in fomr of 1/0, yes/no, true/false

"""

import pandas as pd
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn import datasets


#spliting datasets into train and test
# Load the Diabetes dataset
columns = 'age, sex, bmi, maps, tc, ldl, hdl, tch, ltg, glu'.split()
diabetes = datasets.load_diabetes() # Call the diabetes dataset from sklearn
df = pd.DataFrame(diabetes.data, columns=columns) # load the dataset as a pandas data frame
y = diabetes.target # define the target variable (dependent variable) as y
x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print (x_train.shape, y_train.shape)
print (x_test.shape, y_test.shape)

#estimating accuracy of algorithm
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url,names = names)
array = data.values
x = array[:, 0:8]
y = array[:,8]
kFold = KFold(n_splits = 10, random_state = 7)
model = LogisticRegression()
results = cross_val_score(model, x, y, cv = kFold)
print("Accuracy: %.3f%% (%.3f%%)",(results.mean())*100.0, results.std()*100.0)
