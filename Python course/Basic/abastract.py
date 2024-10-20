from abc import ABC,abstractmethod
#abstract base class

class Animal(ABC):
    @abstractmethod #decorator
    # enforce all derived class to have eat method
    def eat(self):
        print('I need food')
    @abstractmethod
    #inheritated class a define kortei hbe 
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.category='Monkey'
        self.name='Monkey'
        super().__init__()
    
    def eat(self): #abstract nmethod diye inherit kortece
        print('Hey na nana, I am eating Banana')

    def move(self):
        print("Hanging on the brances")
    

    

    

layka=Monkey('lucky')
layka.eat()
layka.move()
