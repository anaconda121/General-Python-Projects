def printLine():
    print("\n")

import numpy as np


np.array([1, 2, 3]) #generating basic numpy array


print(np.zeros(3)) #generates an array with three slots, all with value 0
printLine()

print(np.ones((4,5))) #generates 2-d array with 4 rows and 5 cols
printLine()

print(np.full((5,4), 3.14))#generates 2-d array with 5 rows and 4 cols all values as 3.14
printLine()


#basic numy array stats
size = np.full((5,5), 4)
print(size)
printLine()

print(size.ndim) #number of dimensions
printLine()

print(size.size) #num elements
printLine()

print(size.shape) #prints num of cols, rows
printLine()

print(size.dtype) #what type of data is in array - only one type allowed
printLine()

#random nums
import random 
  
random.seed(3) 
print(random.randint(1, 1000)) 

random.seed(3)
print(random.randint(1, 1000))

random.seed(3)
print(random.randint(1, 1000))
printLine()

#accessing and editing array vals
edit = np.full((5,5), 3)
print(edit)
print(edit[0,1]) #prints val of number in first row, second col slot


edit[0,1] = 222.2 #edited value of number in first row, second col slot
printLine()
print(edit) #array cant hold .2 part b/c only data type in there is int right now

#concatenating arrays
printLine()
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y])) #result: 1 2 3 3 2 1 

#formatting arrays using vertical stacking
printLine()
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
print(np.vstack([x, grid])) #prints array in rows of 3 because first array is in set of 3
printLine()

#formatting arrays using np.arange
print("A\n", np.arange(4).reshape(2, 2), "\n") #prints array with vals 0-3 
print("A\n", np.arange(4, 10, 2) ,"\n") #prints array with vals 4-9 incremented by 2

#basic math functions
x = [-2, -1, 1, 2]

print("Absolute value: ", np.abs(x))
print("Exponential: ", np.exp(x)) #takes e to the power of elements of x
print("Logarithm: ", np.log(np.abs(x))) #takes log of abs value of elements of x

#boolean operations - np.where
y = np.random.rand(3) #2-d array of random nums, 3 rows and 3 cols
printLine()
y > 0.5


#aggregation

#sum all vals
nums = np.random.random(100)
totalSum = np.sum(nums) #sums up all values of nums
print(totalSum)

#sum of a column
cols = np.random.random((3,4))
print("\n", cols)
print("\n sum of all element in columns", cols.sum(axis = 0))
print("\n sum of all element in rows", cols.sum(axis = 1))

#basic statistics functions
print("\n", np.std(cols)) #mean standard deviation
print("\n",np.argmin(cols)) #prints index of the smallest element
print("\n", np.percentile(cols, 50))#prints number in 50 percentile

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

M = np.ones((3, 3))
print("M is: \n", M)
print("M+a is: \n", M+a)
