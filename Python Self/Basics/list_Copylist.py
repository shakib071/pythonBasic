#You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist=thislist.copy()
print(mylist)

#Make a copy of a list with the list() method

mylist1=list(thislist)
print(mylist1)