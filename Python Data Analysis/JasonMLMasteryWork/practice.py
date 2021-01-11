# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:49:36 2020

@author: tanis
"""

from pandas import read_csv
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

url = 'world.csv'
names = ['Country Name','Country Code','Indicator Name','Indicator Code','1970','1971','1972','1973',
         '1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986',
         '1987','1988','1989','1990','1991','1992','1993','1994','1995','1996',
         '1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008',
         '2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'
         ,'2021','2022','2023','2024','2025']

data = read_csv(url,names = names)

print(data.shape)
print(pd.read_csv("world.csv", header = [0]))
print(data.iloc[0:5,:])
print(data.iloc[:,1:])
print(data.index)
print(data[["Country Name", "2020"]])
df = pd.read_csv('world.csv')
print(df.head(10))

#frequency table
print(df['Country Code'].value_counts())

#pivot table
Employees = {'Name of Employee': ['Jon','Mark','Tina','Maria',
                                  'Bill','Jon','Mark','Tina',
                                  'Maria','Bill','Jon','Mark','Tina',
                                  'Maria','Bill','Jon','Mark','Tina','Maria','Bill'],
             'Sales': [1000,300,400,500,800,1000,500,700,50,60
                       ,1000,900,750,200,300,1000,900,250,750,50],
             'Quarter': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
             'Country': ['US','Japan','Brazil','UK','US','Brazil',
                         'Japan','Brazil','US','US','US','Japan','Brazil'
                         ,'UK','Brazil','Japan','Japan','Brazil','UK','US']
            }

df = DataFrame(Employees, columns= ['Name of Employee', 'Sales','Quarter','Country'])
print (df)

#bar chart
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()

#reading data to make pivot table
df = pd.read_csv('world.csv')
df.head()
print(pd.pivot_table(df, index = ['Country Name','Country Code','Indicator Name',
                                  'Indicator Code','1970','1971','1972','1973',
                                  '1974','1975',]))


