
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3=list1+list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one

for x in list2:
    list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



