# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:03:03 2020

@author: tanis
"""

"""LISTS"""

listOne = ["apples", "oranges", "bananas"]
print(listOne)
print(listOne[0])
print(listOne[0:2])
print(listOne[-1]) #prints last item of list
print(listOne[-2])#prints second last item of list
print(listOne[-3])#equal to print(listOne[0]) b/c three indexes in the list 

listTwo = ["one", "two","three", "four", "five"]
print(listTwo[:4]) #prints from index one of the list up to index 4, won't start at index one b/c no start value defined
print(listTwo[1:]) #prints from index one to the end
print(listTwo[-4:-1]) # start list search from the last indexes
listTwo[1] = "six"
print(listTwo) #edit index of the list

listThree = ["dog", "cat", "tiger", "zebra", "fish", "squid", "cheeta"]
for x in listThree: #printing out all the values of the list, each on a separate line, x = number of times loop has iterated
    print (x)
if "dog" in listThree:
    print("Yes")
print(len(listThree)) #length of list
listThree.append("horse") #add index to the end of list
print(listThree)
listThree.insert(1, "snake") #adds snake into index 1
print(listThree)
listThree.remove("snake")
print(listThree)
listThree.pop() #removes last index of the list
print(listThree)
listThree.pop(4) #removes index four of the list, equal to del listThree[4]
print(listThree)
del[listThree] #remove entire list
#print(listThree), gives error b/c list is deleted 

listFour = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete"]
listFour.clear() #empties the list
print(listFour)
newList = list(listFour) #clones a list
print(newList)

#adding lists together
listFive = ["a", "b" , "c"]
listSix = [1, 2, 3]
listSeven = listFive + listSix
print(listSeven)

""" FLOW CONTROL """

# if statement
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("negative")
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('none of the above')
#for loop
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for i in range(5):
    print (i)
for i in range(0,10,3):
    print(i)
print(sum(range(4)))# prints sum of 0+1+2+3

#factorial function
def factorial(n):
    factorial = 1
    for i in range(1,n+1): 
        factorial = factorial * i 
    print (factorial) 

#prime number function
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n,"is not prime" )
            break
    else:
        print(n, 'is a prime number')

""" NUMPY ARRAYS and PANDAS DATAFRAMES"""
import numpy
import pandas
myArray = numpy.array([[1,2,3], [4,5,6]])
rowNames = ['a','b']
columnNames = ['one','two','three']
myDataFrame = pandas.DataFrame(myArray, index = rowNames, columns = columnNames)
print(myDataFrame)
#above code prints out table with a and b as rows and one, two, three as columns
""" MATPLOTLIB"""
from matplotlib import pyplot as plt
#line plot
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
plt.plot(x,y)
plt.show()
#bar plot
plt.bar(x,y)
plt.show()
#histogram
plt.hist(y)
plt.show()
#scatterplot
plt.scatter(x,y)
plt.show()