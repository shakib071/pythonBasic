from fooditem import FoodItem
from menu import Menu
from resturant import Resturant
from user import Customer ,Admin,Employee
from orders import Order


mamar_resturant=Resturant("mamar_resturant")

def customer_menu():
    name=input("Enter you name: ")
    email=input("Enter your Email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address :")
    customer=Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {customer.name}')
        print("1. View menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")


        choice=int(input("Enter Your Choice: "))

        if choice==1:
            customer.view_menu(mamar_resturant)

        elif choice==2:
            item_name=input("Enter Item name: ")
            item_quantity=input("Enter Item Quantity : ")
            customer.add_to_cart(mamar_resturant,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()

        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid Input")


def Admin_menu():
    name=input("Enter you name: ")
    email=input("Enter your Email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address :")
    admin=Admin(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {admin.name}')
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")


        choice=int(input("Enter Your Choice: "))

        if choice==1:
            item_name=input("Enter item name: ")
            item_price=int(input("Enter item price"))
            item_quantity=int(input("Enter item quantity"))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_resturant,item)

        elif choice==2:
            name=input("Enter employee name : ")
            phone=input("enter your phone: ")
            email=input("Enter Your Email : ")
            designation=input("Enter your designation")
            age=input("Enter your age")
            salary=input("Enter Your Salary: ")
            address=input("Enter Your addrsss: ")
            employee=Employee(name, phone, email, address,age,designation,salary)
            admin.add_employee(mamar_resturant,employee)
        elif choice==3:
            admin.view_employee(mamar_resturant)

        elif choice==4:
            admin.view_menu(mamar_resturant)
        elif choice==5:
            item_name=input("Enter item name: ")
            admin.remove_item(mamar_resturant,item_name)
        elif choice==6:
            break
        else:
            print("Invalid Input")
        
while True:
    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice=int(input("Enter Your choice: "))

    if choice==1:
        customer_menu()
    elif choice==2:
        Admin_menu()
    elif choice==3:
        break
    else:
        print("Imvalid Input")
    
