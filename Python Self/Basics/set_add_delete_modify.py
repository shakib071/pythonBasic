#Python - Add Set Items
thisset = {"apple", "banana", "cherry"}
#To add one item to a set use the add() method.
thisset.add("Orange")
print(thisset)



# Add Sets
# To add items from another set into the current set, use the update() method

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)



#Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)
#If the item to remove does not exist, remove() will raise an error.
#acea kina check kore delete korte hbe

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#If the item to remove does not exist, discard() will NOT raise an error.
#acea kina check kore delete korte hbe




# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item
#Remove a random item by using the pop() method
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed

thisset = {"apple", "banana", "cherry"}
x=thisset.pop()
print(x)
print(thisset)



#The clear() method empties the set

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)#error because set doesnot exist anymore














