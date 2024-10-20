# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

thistuple=("apple","banana","cherry","alu")
print(thistuple)

#Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#Since tuples are indexed, they can have items with the same value

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#A tuple with strings, integers and boolean values

tuole1=("sada",32,True,40,"male")
print(tuole1)

#It is also possible to use the tuple() constructor to make a tuple

thistuple1=tuple(("apple","banana","cherry"))
print(thistuple1)

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Set items are unchangeable, but you can remove and/or add items whenever you like

print(thistuple1[1]) #index starts at 0
print(thistuple1[-1])#last theke 1st

print(thistuple1[0:2])


#To determine if a specified item is present in a tuple use the in keyword
#Check if "apple" is present in the tuple

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes Alu")



#Convert the tuple into a list to be able to change it

y=list(thistuple)
print(y)






