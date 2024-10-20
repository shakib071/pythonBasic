x=1 #int
y=2.4 #float
z=1j #complex

print(x)
print(y)
print(z)
print(type(x),type(y),type(z))

#scintific float 
x1=35e4
y1=12E4
z1=-87.3e100
print(x1,y1,z1)
print(type(x1),type(y1),type(z1))#float Type


x2=3+5j
y2=5j
z2=-5j
print(type(x2),type(y2),type(z2))

#conversion

a=float(x) #convert to Float
b=int(y) #convert to int
c=complex(x) #convert to complex

print(a,b,c)
# d=int(z) #complex cannot be convert to any other form


