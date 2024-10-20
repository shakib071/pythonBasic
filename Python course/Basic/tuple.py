#tuple is a sequence
#Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created.

def multiple():
    return 3,4#its a tuple

print(multiple())
#tuple has 1st bracket
#list has 3rd bracket

things='pen','tripod','water' #tuple
things1=['pen','tripod','water']#list

print(type(things))

print(type(things1))

print(things[0])
print(things[-2])
print(things[1:2])

#tuple cant be changed

#
mega=([2,3,5],[6,7,8,9])
#tuple which contains list
print(type(mega))#tuple
print(mega[0])
mega[0][1]=666
#tuple cant be changed but the list inside the tuple can be changed
print(mega)

t=('dff','dff','trt')#tuple



