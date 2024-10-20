
# def sum(num1,num2,num3=0,num4=0):
#     return num1+num2+num3+num4
# #num3=0 howyay jodi perameter a value na dei tahole 0 dhore kaj korbe
# # ar value dile oi value niye kaj korbe
# #mane =0 diye optional hoye jay
# total=sum(10,11,10)
# print("total:",total)

#args
#amra jani na koyta perameter a value jabe

def all_sum(*numbers):
    #jotogula issa totogula perameter dite pari
    #onekta arra ba tuple er moto kaj kobe

    for num in numbers:
        print(num)

total=all_sum(45,56,43,3,43,323)
print(total)

#or
def all_sum(num1,num2,*numbers):
    #1st 2 ta num1,num2 hisebe nebe
    print(numbers)
    for num in numbers:
        print(num)

total=all_sum(45,56,43,3,43,323)
print(total)