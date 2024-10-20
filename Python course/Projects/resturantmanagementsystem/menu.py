class Menu:
    def __init__(self) -> None:
        self.items=[] #items er database

    def add_menu_item(self,item):#fooditem class er constractor
        self.items.append(item)
    
    def find_item(self,item_name):
        for item in self.items:
            if item_name.lower()==item_name.lower():
                return item
            return None
        
    def remove_item(self,item_name):
        item=self.find_item(item_name)

        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item Not Found")
    
    def show_menu(self):
        print('*****MENU*****')
        print("Name\tPrice\tQuantity")

        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

