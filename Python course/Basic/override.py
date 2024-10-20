class person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print("vaat mangsho")
    
    def exercise(self):
        raise NotImplementedError #ekhon child class a implement na korle error debe
    #mane child class forcefully implement kortei hbe
    #child class a ei exercise method ta implement kortei hbe 



class Cricketer(person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)
    
    def eat(self):
        print('vegetable')#override korlo parent class er eat k
    
    def exercise(self):
        print("Gym a poisa dia hudai gham jhoray")

    # + operator overload
    
    def __add__(self,other):
        return self.age+other.age
    # * operator overload
    def __mul__(self,other):
        return self.weight*other.age
    # len overload
    def __len__(self):
        return self.height
    # > operator overload
    def __gt__(self,other):
        return self.age>other.age
    
    

shakib=Cricketer('Shakib',37,78,56,'BD')
mushi=Cricketer('mushi',334,56,4,"BD")
# shakib.eat()
# shakib.exercise()

#https://docs.python.org/3/reference/datamodel.html
#https://www.geeksforgeeks.org/dunder-magic-methods-python/

# plus sign overload
print(45+23)
print('shakib'+ 'rakib')
print([12,98]+[5,6,7,8,9])
print(shakib+mushi)# __add__ method use korle plus sign use kora jabe
print(shakib*mushi)
print(len(shakib))
print(shakib<mushi)
    
        