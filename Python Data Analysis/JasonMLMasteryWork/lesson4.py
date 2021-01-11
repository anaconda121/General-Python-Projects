# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:24:47 2020

@author: tanis
"""
from pandas import read_csv
import pandas as pd
#describe function, calculates averages for all headings
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url,names = names)
description = data.describe()
print(description)
#corr method
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
data.dropna(inplace = True)  
perc =[.20, .40, .60, .80] #prints percentailes
include =['object', 'float', 'int'] 
desc = data.describe(percentiles = perc, include = include) 
print(desc) 
print(data.corr(method = "kendall")) #kendall is a data analysis method, finds trends
print(data.corr(method = "pearson"))#perason is a data analysis method, The nearer the scatter of points is to a 
#straight line, the higher the strength of association between the variables

#dtypes method, prints out data type of each header
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71], 
                   'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'], 
                   'Age':[14, 25, 55, 8, 21]}) 
result = df.dtypes 
print(result)
#head command, prints out first 10 rows
answer = pd.read_csv('https://goo.gl/bDdBiA')
print(answer.head(10))
                       
#frequency table, saying how many times certain word or number is in the dataset
             