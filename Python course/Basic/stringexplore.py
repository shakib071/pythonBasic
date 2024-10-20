name='shakib khan'
name2="Shakib Khan"
name3="""
shakib khan
number one
"""
#multi line string

print(name)
print(name2)
print(name3)

name4='Shakib\'s Khane' #escape 
#\ will not print
print(name4)

#string is a sequence of char
for char in name2:
    print(char)
#mutable is changeable(list)
#immutable means unchangable(string)
# name2[0]='R'#you cant its immutable
# print(name2)

if 'Khan' in name2:
    print("Exists")

print(name2.upper())
print(name2)