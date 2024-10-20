# #take parameters in order
# #serial wise
# def full_name(first,last):
#     name=f'full name is: {first} {last}'
#     return name 

# name=full_name("Shakib","Hasan")

# print(name)

# #not serial wise perameter

# def full_name(first,last):
#     name=f'full name is: {first} {last}'
#     return name 

# name=full_name(last="Hasan",first="shakib")
# print(name)

# #args er moto kore
# def full_name(first,last,*additioal):
#     name=f'full name is: {first} {last}'
#     return name 

# name=full_name("Shakib","Hasan")

# print(name)

#kargs a 2 ta ** dewya hoy
#kargs bola hoy karon ekhane call korar somoy key oo dewya hoy

# def full_name(first,last,**additional):
    
#     print(additional)
#     #aditional ba kargs er moddhe ja chilo segula print hbe
#     print(additional['title'])
#     #ekhaen additionaler moddhe title ta print korbe shudhu
    
#     for key,value in additional.items():
#         print(key,value)
    



#     name=f'full name is: {first} {last}'
#     return name 

# name=full_name(first="Shakib",last="Hasan",title="Student",additional="Abal")

# print(name)

##def functionname(n1,n2,*args,**kargs)



# #multiple return

# def a_lot(num1,num2):
#     sum=num1+num2
#     mul=num1*num2
#     sub=num1-num2
#     return sum,mul,sub

