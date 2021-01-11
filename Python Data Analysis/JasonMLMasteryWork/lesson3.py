# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:22:58 2020

@author: tanis
"""

#load data from csv
from pandas import read_csv
import pandas as pd
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url,names = names)
print(data.shape)
#loading data from downloaded file
url = 'superbowl.csv'
names = ['Date','SB','Winner','Winner Pts','Loser','Loser Pts','MVP','Stadium','City,State']
dataTwo = read_csv(url,names = names)
print(dataTwo.shape)
#header, makes number of rows defined in header above 0
print(pd.read_csv("superbowl.csv", header = [0]))
#iloc command, prints certain part of dataset, here first five rows and all columns
print(dataTwo.iloc[0:5,:])
print(dataTwo.iloc[:,1:])
#index function
print(dataTwo.index)
#print out certain columns of the dataset
print(dataTwo[["Date", "SB"]])
