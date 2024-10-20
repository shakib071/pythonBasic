#list-->[]
#tuple-->()
#set-->{}

# set : unique items collection
numbers=[12,56,34,56,45,45,34,55,55]
print(numbers)
numbers_set=set(numbers)
print(numbers_set)
numbers_set.add(557)
#icchamoto jaygay add hbe
#sequence maintain korbena

print(numbers_set)

# numbers_set[1]=5 # cant be possible
#we can add or delete in set but we cant manupulate positionwise

numbers_set.remove(55)
print(numbers_set)

A={1,3,5,7}
B={1,2,3,4,5}
print(A&B) #intersection
print(A|B)#union
