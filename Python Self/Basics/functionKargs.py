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

# everything=a_lot(55,21)
# print(everything) #tuple akare hbe






def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

