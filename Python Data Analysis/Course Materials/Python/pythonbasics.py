class Book:
    
    def __init__(self, title, author, numberOfPages, publisher):
        #self refers to current class, in this case, book class
        self.title = title
        self.author = author
        self.numberOfPages = numberOfPages
        self.publisher = publisher

        
#creating an instance of book class
testBook = Book("Diary of a Wimpy Kid", "Jeff Kinney" , 250, "randomHouse")
print(testBook.title)

#edit attributes of class
testBook.author = "Tanish Tyagi"
print(testBook.author)

testScores = [98.1, 95.6, 89, 91, 100]
testScores[0] = 99;
print(testScores[0])
print(testScores[-1]) #prints last element
print(testScores[-2]) #prints second last element
print(testScores[1:4]) #prints values of index 1 -4
sum(testScores) #adds up sum of all elements in list

import sys
guests = ["Joey", "Martin", "Marie"]
print(str(sys.getsizeof(guests)))
guests.append(7) #adds seven to end of list
guests.insert(1, "Tanish") #replaces index 1 with Tanish
guests.remove("Tanish") #removes element with value Tanish
print(guests.index(7)) # print index with value 7
del guests[0] #deletes value of first element
print(guests)
len(guests) #prints number of elements

# TODO Step 1 - Replace the ?? by the proper code to create an empty list
guests = []

# TODO Step 2 - Add Joey, Martin and Marie to the list
guests = ["Joey", "Martin", "Marie"]
# TODO Step 3 – display the size of the list
print(str(sys.getsizeof(guests)))
# TODO Step 4 - Replace Martin with John in the list
guests[1] = "John"
# TODO Step 5 - Remove Joey from the list
guests[0] = "";

# print the content of the list
for guest in guests :
	print(guest)

dictionary = {"Tanish": "Tansih", "Riya": 2, "Urvashi": 45} #value in quotes is the key, next value is value
print(dictionary["Tanish"])
dictionary["Tanish"] = 45; #replacing value of key Tanish with 45
dictionary.pop("Tanish") #deltes key Tanish and value associated with Key Tanish
print(dictionary)

basket = ["apple", "orange", "banana"]

for fruit in basket:
    if fruit == "orange":
        print("I have an", fruit, "!")
        break
    else:
        print("no")

numberOfTrees = 0

while numberOfTrees < 10:
    numberOfTrees += 1
    print("I planted", numberOfTrees, "trees")
    
print("I have a forest!")

string = "simple"

print(string.upper()) #prints string in all caps
print(string.lower()) #prints string in all lowercase
print(string.capitalize()) #capitalizing first letter of string
print(string.count("s")) #counts instance of letter s
print(string.replace("simple", "tanish")) #replaces word simple with Tanish

myList = [1, 2, 1000, 289, 40.2, -20]
myDict = {'apple': 4, 'orange': 2, 'strawberry':10}

myList.sort() # sort and replace the list, not returning any value
print(myList) # -> -20, 1, 2, 40.2, 289, 1000

myList.pop(3)
print(myList) # -> -20, 1, 2, 289, 1000

myDict.pop('apple')
print(myDict) # -> only orange and strawberry

mySecondList = myDict.values()
print(mySecondList) # -> [2, 10]