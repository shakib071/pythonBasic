# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

thisset={"apple","banana","cherry"}
print(thisset)
#Sets are unordered, so you cannot be sure in which order the items will appear.

#Set items are unordered, unchangeable, and do not allow duplicate values.

thisset= {"apple", "banana", "cherry", "apple"}
print(thisset) #{'apple', 'cherry', 'banana'}

#The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset={"Apple","Banana","cherry",True,1,2}
print(thisset) #1 is removed because true is also count as one


# False and 0 is considered the same value
#The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#To determine how many items a set has, use the len() function
print(len(thisset))

# Using the set() constructor to make a set

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.