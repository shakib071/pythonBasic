# #base class,parent class

# class BaseClass:
#     pass

# #derived class or child class 
# class DerivedClass(BaseClass):
#     pass

# """
# 1.Simple inheritance : parent class -->Child class (Gadget---> Phone)
# 2.Multilevel inheritance : Grandpa -->parent -->Child -->child(vehicle-->Bus-->ACB)
# """

class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
    
    def __repr__(self) -> str:
        return f'{self.name,self.price}'
    
    def move(self):
        pass

class Bus(Vehicle):#inheritance
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):#inheritance

    def __init__(self, name, price,weight) -> None:
        self.weight=weight
        super().__init__(name, price)

class PickUpTruck(Truck):#multilevel inheritance
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)
    
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
    
green_line=ACBus('green',500000,20,17)
print(green_line)
print(green_line.temperature)




