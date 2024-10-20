#module kichui na khali ek file onno file a import kora

#import mymodule as mx
#ekhane mymodule file k j file a import korbo sekhane mx 
#name dakleoo same hbe
#mane rename koreteci






#build in modules

import platform

x = platform.system() #platform er nam debe(windows)
print(x)

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function
import platform
#plaform function er moddhe j j function acea variable acea setar nam debe
x = dir(platform)
print(x)

#The dir() function can be used on all modules, also the ones you create yourself.


#python Datetime

import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #ajke ki bar seta debe


x = datetime.datetime(2020, 5, 17) #specific date x a add korbe
print(x)


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))#ki mas set debe

#aro method notion a acea








