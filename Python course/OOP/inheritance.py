
#base class ,parent class,common Attributes + functionality class
#derived class->child class


class Gadget:#base class
    def __init__(self,brand,price,color,origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin


    def run(self):
        return f'Running Laptop: {self.brand}'
    
#common jinish gula ekjaygay base class a rakhbo
#repetation kom hbe



class Laptop:
    def __init__(self,memory):
       
        self.memory=memory


    def coding(self):
        return f'Learning Python and Practicing'
    

class Phone(Gadget):#Gadget er shathe relationship korlam
    #inheriate
    def __init__(self,brand,price,colour,origin,sim):
        self.sim=sim
        super().__init__(brand,price,colour,origin)
        #passing to the base Class


   
    def phone_call(self,number):
        return f'Calling :{number}'
    
    def __repr__(self) -> str:
        return f'phone: {self.sim},{self.brand}'
    

# my_phone=Phone(True)
my_phone=Phone('Iphone',120000,'silver','china',True)
print(my_phone)
print(my_phone.brand,my_phone.color)
    

