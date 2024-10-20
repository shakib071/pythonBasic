# #args
# #amra jani na koyta perameter a value jabe

# def all_sum(*numbers):
#     #jotogula issa totogula perameter dite pari
#     #onekta arra ba tuple er moto kaj kobe

#     for num in numbers:
#         print(num)

# total=all_sum(45,56,43,3,43,323)
# print(total)

# #or
# def all_sum(num1,num2,*numbers):
#     #1st 2 ta num1,num2 hisebe nebe
#     print(numbers)
#     for num in numbers:
#         print(num)

# total=all_sum(45,56,43,3,43,323)
# print(total)



#Arbitrary Arguments, *args

def my_func(*args):
    for x in args:
        print(x)

my_func(10,20,39,43,54,56,32,87)

#jotogula iccha perameter dite pari