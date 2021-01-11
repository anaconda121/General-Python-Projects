from sklearn import datasets
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

plt.style.use('ggplot')
iris = datasets.load_iris()
print(type(iris)) #dataset type = bunch, similar to a dictionary
print(iris.keys())
