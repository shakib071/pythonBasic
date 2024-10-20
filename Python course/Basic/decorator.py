import math
import time

def timer(func):
    def inner(*args,**kwargs):#shudhu n oo use kora jabe
        start=time.time()
        print('time started')
        # print(func)
        func(*args,**kwargs) #shudhu n oo use kora jabe

        print(" time ended")
        end=time.time()
        print(f'total time taken {end-start}')
    return inner

# timer()()

@timer  #timer a get_factorial pass korbe its a decorator
def get_factorial(n):
    print('factorial starting')
    result=math.factorial(n)
    print(f'factorial of {n} is:{result}')
#esier way to decorate
# get_factorial(120)
get_factorial(n=1000)
#vegal way to decorate
# timer(get_factorial)()
