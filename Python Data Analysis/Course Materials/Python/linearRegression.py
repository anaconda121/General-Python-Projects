import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import linear_model
import pandas as pd

"""
Linear Regression - a straight line of best fit genereated by that values of 
x and y values. Positive relationship is both independant (x) and dependent
(y) values increase. Negative relationship if independent val increases
but dependent val decreases. 

Formula: b0 + b1 * x == y= mx + b
	b0 = y-intercept
	b1 = slope
	x = x-value
"""

#loading datasets
hubble = pd.read_csv('Datasets/hubble_data.csv')

#graphing dataset

#matplotlib
hubble.plot(x = 'distance', y = 'recession_velocity', style = 'o')
plt.title('Hubble')  
plt.xlabel('distance')  
plt.ylabel('recession_velocity')  
plt.show()

#seaborn
sns.pairplot(hubble, height = 2.5)
plt.show()

#trying to find average recession_velocity
plt.figure(figsize=(15,10))
plt.tight_layout() #formats better
sns.distplot(hubble['recession_velocity'])
plt.show()
"""
Based on graphing the dataset, we can conclude that this dataset 
is an example of positive linear regression.
"""

print(hubble.describe()) #prints dataset stats
print(hubble.shape) #prints out num of rows and cols in the dataset

"""
Dividing into Atrributes and Labels

Attributes are the independent variables while labels are  dependent variables 
whose values are to be predicted. 

This model ist trying to predict that reccesion_velocity based on the distance recorded
"""

X = hubble['distance'].values.reshape(-1, 1)
y = hubble['recession_velocity'].values.reshape(-1,1)

#splitting data into training sets and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#training algorithm
regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
accuracy = regressor.score(X_test, y_test)
print("Accuracy: ", accuracy)

#To retrieve the intercept:
print(regressor.intercept_)

#For retrieving the slope:
print(regressor.coef_)

#start making predictions
y_pred = regressor.predict(X_train)


#printing graph
plt.scatter(X, y,  color='gray')
plt.plot(X_train, y_pred, color='red', linewidth=2)
plt.show()