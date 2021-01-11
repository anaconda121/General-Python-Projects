# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:21:26 2020

@author: tanis
"""

#how to prepare data for modeling and 

#use scale and center options to standarize data
#normalize data using range option

#from sklearn.preprocessing import StandardScaler
#from pandas import read_csv
import numpy as np
from sklearn.impute import SimpleImputer
"""
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url,names = names)
array = data.values
x = array[:,0:8]
y = array[:,8]
scaler = StandardScaler().fit(x)
rescaledx = scaler.transform(x)
numpy.set_printoptions(precision=3)
print(rescaledx[0:5,:])
"""
#finding missing values in datasets

  
# Importing the SimpleImputer class 

  
# Imputer object using the mean strategy and  
# missing_data type for imputation 
imputer = SimpleImputer(missing_data = np.nan,  strategy ='mean') 
data = [[12, np.nan, 34], [10, 32, np.nan],[np.nan, 11, 20]] 
print("Original Data : \n", data) 
# Fitting the data to the imputer object 
imputer = imputer.fit(data) 
# Imputing the data      
data = imputer.transform(data) 
print("Imputed Data : \n", data) 