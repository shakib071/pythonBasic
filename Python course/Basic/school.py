class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.id=id
        self.current_class=current_class

    def __repr__(self) -> str:#repesentation
        return f'Student Name {self.name},class :{self.current_class}'


alia=Student('Alia Torkari',9,1)

print(alia)
