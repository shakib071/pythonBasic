#The remove() method removes the specified item.

thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurance

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.

thislist.pop()
print(thislist)

#The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]

del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.

# del thislist
# print(thislist) #name 'thislist' is not defined

#The clear() method empties the list.
thislist.clear()
print(thislist)