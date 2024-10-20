#singleton --> one single instance

#if you want a new instance , you will get the old one (Already Created) instance

#factory #do factory
#builder eigula google a  dekhe porte hbe
#https://www.geeksforgeeks.org/factory-method-python-design-patterns/
#https://www.geeksforgeeks.org/observer-method-python-design-patterns/

class Singleton:
    __instance=None

    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance=self
        else:
            raise Exception('This is  singleton , Already have a instance ,use that one by call get_instance method')
    
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
first= Singleton.get_instance()
second=Singleton.get_instance()
third=Singleton.get_instance()
print(first)
print(second)
print(third)
last=Singleton() 
        