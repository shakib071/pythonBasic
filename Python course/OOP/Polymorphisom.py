#poly -->many
# morph -->shape

class Animal:
    def __init__(self,name) -> None:
        self.name=name

    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('ghew ghew')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('beeh beeh')
    
        
    
    
don=Cat('real don')
don.make_sound()

shepard=Dog('Local Shepard')
shepard.make_sound()

mess=Goat('L M')
mess.make_sound()

less=Goat('gora gori khay')

animals=[don,shepard,mess,less]

for animal in animals:
    animal.make_sound()



        