
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"Vai") #insets "Vai" in index 2
print(thislist)

# To add an item to the end of the list, use the append() method

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #last a add korbe
print(thislist)

#To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical) #add tropical to last of thislist
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple=("ghjsdgf","gsdhjfgas")
thislist.extend(thistuple) #thislist a tuple ta dhukaiya tuple ta ke list a convert korbe
print(thislist)

