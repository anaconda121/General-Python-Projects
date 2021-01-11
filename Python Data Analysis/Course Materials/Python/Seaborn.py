import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#loading datasets
iris = sns.load_dataset('iris')
iris.head() #see first 5 rows of datasets

sns.pairplot(iris, hue = 'species', height = 2.5)

#jointplot is a combination of scatterplot and histogram
with sns.axes_style('dark'):
    sns.jointplot("petal_length", "petal_width", data=iris, kind = "reg") #kind gives line of best fit

"""
generate advanced graphs
hue means that filters reseults based on spieces, and compares all 
other headers in dataset

How to read pairplot graphs:
    like a matrix - x and y axis
    when 2 headers of the same type are matched, histogram is generated
    for other elements, get bivariate scatterplots
"""

sns.set()
x = np.linspace(0, 10, 500)
y = np.random.randn(500)
plt.figure(figsize=(3, 3)) 
plt.plot(x,y)
plt.show()

#distplot - combo of bargraph and distribution
sns.set(); 
x = np.random.randn(100)
ax = sns.distplot(x, kde = True) #kde rounds distribution curve
plt.show()