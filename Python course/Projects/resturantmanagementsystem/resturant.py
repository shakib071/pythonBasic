from menu import Menu
class Resturant:
    def __init__(self,name) -> None:
        self.name=name
        self.employees=[] #eta hocce employee database
        self.menu=Menu()

    def add_employee(self,employee): #employee object pass korbo
        self.employees.append(employee)
        print(f'{employee.name} Added')
    
    def view_employee(self):
        print("Employee List !!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)


