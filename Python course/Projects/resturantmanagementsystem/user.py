#customer
#Employee
#Admin-> Add delete

from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address


class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def view_menu(self,resturant):
        resturant.menu.show_menu()

    def add_to_cart(self,resturant,item_name,quantity):
        item=resturant.menu.find_item(item_name)

        if item:
            if quantity>item.quantity:
                print("Item quantity Exceeded")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print('item added')
        else:
            print("Item not found")
    
    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")

        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f'To+
        tal {self.cart.total_price} paid succesfully')
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary) -> None:
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary


class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)

    def add_employee(self,resturant,employee):#Resturant Class and employee is an object
        resturant.add_employee(employee)

    

    def view_employee(self,resturant):
        resturant.view_employee()

    def add_new_item(self,resturant,item):
        resturant.menu.add_menu_item(item)
    

    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

    def view_menu(self,resturant):
        resturant.menu.show_menu()
    





# emp=Employee('Rahim',1923432,"rahim@gmail.com",'Dhaka',12,'Manager',300)
# print(emp.age)
# print(emp.name)


# ad=Admin('karim','123445',"karim@gmail.com",'Dhaka')
# ad.add_employee('sagor','sagor@gmail.com','23234','Dhaka',12,'Chamcha',123434)

# ad.view_employee()














