#common func
# def double(x):
#     return x*2

#lambda func

doubled=lambda num : num*2
#variable name= labda perameter : return value

result=doubled(44)
print(result)
squared=lambda num : num*num

numbers=[12,32,3,43,4,5,454,343,43]

doubled_nums=map(doubled,numbers)
# print(doubled_nums)#output ibject debe tai bujha jabe na

print(numbers)
print(list(doubled_nums))#list kore print

square_nums=map(lambda x:x*x,numbers)
print(numbers)
print(list(square_nums))

actors = [
    {'name':'sabana','age':10},
    {'name':'sab','age':20},
    {'name':'saban','age':62},
    {'name':'saba','age':30},
    {'name':'sa','age':6}
]

jouniors=filter(lambda actor : actor['age']<40,actors)
fivers=filter(lambda actor : actor['age']%5==0,actors)
print(list(jouniors))
print(list(fivers))







