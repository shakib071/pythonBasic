# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3=set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result

set4=set1 | set2
print(set4)

#Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset=set1.union(set2,set3,set4)
print(myset)



#When using the | operator, separate the sets with more | operators
#Use | to join two sets

myset1=set1 | set2 | set3 | set4
print(myset1)


#Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set

x = {"a", "b", "c"}
y = (1, 2, 3)

z=x.union(y)
print(z)



#Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)



# Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.intersection(set2) #common gula #math er motoi
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1 & set2
print(set3)
#  The & operator only allows you to join sets with sets, and not with other data types like you can with the intersecton() method.



# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set

set1.intersection_update(set2)
print(set1)


#The values True and 1 are considered the same value. The same goes for False and 0
#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)




#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set1.difference(set2) #set er minuse er moto
print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.

set3 = set1 - set2
print(set3)

#  The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.



# Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set1.symmetric_difference(set2) #2ta set a common nai seigula
print(set3)


#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set4= set1 ^ set2
print(set4)
#The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)






