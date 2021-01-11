# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:45:12 2020

@author: tanis
"""
import matplotlib.pyplot as plt
from matplotlib import pyplot as p
from pandas import read_csv
from pandas.plotting import scatter_matrix
import numpy as np


#scatter plot function
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url,names = names)
scatter_matrix(data)
plt.show()

#histogram
plt.hist(data)
plt.show()

#box and whisker plots

#create data
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 10) #first value = average
collectn_2 = np.random.normal(80, 30, 20) #second value = mean standard devaition
collectn_3 = np.random.normal(90, 20, 30) #third value = number of nums desired
collectn_4 = np.random.normal(70, 25, 40)
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

#create the boxplot
figure = plt.figure(1, figsize= (9,6))
axes = figure.add_subplot(111)
boxplot = axes.boxplot(data_to_plot)

#normal graph
p.plot(data)
p.show()