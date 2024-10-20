
mylist= ["ghdghs","sdghsyh",3,34]

print(mylist)
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

print(len(mylist))

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# It is also possible to use the list() constructor when creating a new list.


# Using the list() constructor to make a List

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Print the second item of the list

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Remember that the first item has index 0.
#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist=["fdfsd","dfasfasd","dfsaf"]
thislist[1]="shakib" #changes index 1 
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:4]=["ghasgdsad","hgasjgasj","asdgdhasg"] #changes index 1 to 3 (4not included)
print(thislist)

thislist[1:4]=["ALU"] #changes index 1 to 3 with "ALU"
print(thislist)

