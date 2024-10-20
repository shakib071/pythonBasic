#https://www.geeksforgeeks.org/getter-and-setter-in-python/

#read only -> you cannot set the value.value cant be changed
#getter->get the value of a property most of the time you will get the value of a private attribute
#setter -->set a value of a property  through a method ,most of the time ,you will set the value of a private property


class User:

    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    
    #getter without any setter is a read only attribute

    @property
    def age(self): #its now a attribute
        return self._age
    
    @property
    def salary(self): #its like a gettter
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value<0:
         return 'salary cant be negetive'
        self.__money+=value

        


    
samsu=User('Kopa',21,12000)
# print(samsu.__money)#private property use kora jabe na
# print(samsu.age())
print(samsu.age) #@property use er por eta kora jabe
# print(samsu.salary())#method
print(samsu.salary) #@property its only read
# samsu.salary=43435 #its not possible its a getter only read 
samsu.salary=45000 #setter use er por 
print(samsu.salary)


