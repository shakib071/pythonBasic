class Laptop:
    def __init__(self,brand,colour,memory):
        self.brand=brand
        self.colour=colour
        self.memory=memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'Learning Python and Practicing'
    

class Phone:
    def __init__(self,barnd,price,color):
        self.brand=barnd
        self.price=price
        self.color=color
    
    def run(self):
        return f'Phone tipai chokh gelo'
    
    def phone_call(self,number):
        return f'Calling :{number}'
    
