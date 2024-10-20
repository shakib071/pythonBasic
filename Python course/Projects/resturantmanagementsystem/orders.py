class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            self.items[item] +=item.quantity #jodi item ta cart alread thake

        else:
            self.items[item] =item.quantity #cart a fresh add korlam
    
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    
    @property #ekhon total price func variable er moto use kora jabe
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items() )

        
    def clear(self):
        self.items= {}

    



