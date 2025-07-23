
"""
Final Assignment Program - Standalone
Includes all logic, classes, and functionality in one file.
"""

import csv

# ----------- CLASSES -----------
class DeskSp:
    def __init__(self, item_name, quantity, unit_price):
        self._item_name = item_name
        self._quantity = quantity
        self._unit_price = unit_price
        self._total = 0
        self.set_total()

    def set_total(self):
        self._total = self._quantity * self._unit_price

    def __repr__(self):
        return f"{self._item_name:<20}{self._quantity:<12}{self._unit_price:<12.2f}{self._total:<12.2f}"

    def get_item_name(self): return self._item_name
    def get_quantity(self): return self._quantity
    def get_unit_price(self): return self._unit_price
    def get_total(self): return self._total

    def set_quantity(self, quantity):
        self._quantity = quantity
        self.set_total()

    def set_unit_price(self, unit_price):
        self._unit_price = unit_price
        self.set_total()

class OfficeSp(DeskSp): pass
class ComSp(DeskSp): pass

# ----------- FUNCTIONS -----------

def create_instance(inventory):
    desk_items, office_items, com_items = [], [], []
    for category, items in inventory.items():
        for name, data in items.items():
            qty = data["Quantity"]
            price = data["Unit Price"]
            if category == "Desk Supplies":
                desk_items.append(DeskSp(name, qty, price))
            elif category == "Office Equipment":
                office_items.append(OfficeSp(name, qty, price))
            elif category == "Computer Accessories":
                com_items.append(ComSp(name, qty, price))
    return desk_items, office_items, com_items

def write_instance(obj_list, category_name):
    filename = f"{category_name.replace(' ', '_')}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Quantity", "Unit Price", "Total"])
        for obj in obj_list:
            writer.writerow([
                obj.get_item_name(),
                obj.get_quantity(),
                f"${obj.get_unit_price():.2f}",
                f"${obj.get_total():.2f}"
            ])

def category(obj_list):
    print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price"}')
    for obj in obj_list:
        print(f'{obj.get_item_name():<25}{obj.get_quantity():<15}${obj.get_unit_price():.2f}')

def get_item(obj_list):
    item = input("Enter Item (first letter MUST be capitalized): ")
    found = False
    for obj in obj_list:
        if obj.get_item_name() == item:
            print(f'\n{"Item":<25}{"Quantity":<15}{"Unit Price":<15}{"Total"}')
            print(f'{obj.get_item_name():<25}{obj.get_quantity():<15}${obj.get_unit_price():<14.2f}${obj.get_total():.2f}')

            filename = f"{item.replace(' ', '_')}.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Item Name", "Quantity", "Unit Price", "Total"])
                writer.writerow([
                    obj.get_item_name(),
                    obj.get_quantity(),
                    f"${obj.get_unit_price():.2f}",
                    f"${obj.get_total():.2f}"
                ])
            found = True
            break
    if not found:
        print(f"\nThe {item} entered was NOT found!")

def update(obj_list, item):
    for obj in obj_list:
        if obj.get_item_name() == item:
            choice = int(input("What would you like to update?\n1) Quantity\n2) Price\n3) Both\n"))
            if choice == 1:
                qnt = int(input("Enter new Quantity: "))
                obj.set_quantity(qnt)
            elif choice == 2:
                price = float(input("Enter new Price $"))
                obj.set_unit_price(price)
            elif choice == 3:
                qnt = int(input("Enter new Quantity: "))
                price = float(input("Enter new Price $"))
                obj.set_quantity(qnt)
                obj.set_unit_price(price)
            else:
                print("Invalid option!")
            print("Update complete.")
            return
    print(f"\nThe {item} entered was NOT found!")

# ----------- MENU & MAIN -----------
def menu():
    print("\n---------Menu---------")
    print("1) Display Inventory Content")
    print("2) Category Lookup")
    print("3) Item Lookup")
    print("4) Update Item Info")
    print("5) Exit")
    print("----------------------\n")

def main():
    inventory = {
        "Desk Supplies": {
            "Pens": {"Quantity": 150, "Unit Price": 3.45},
            "Pencils": {"Quantity": 200, "Unit Price": 1.50},
            "Markers": {"Quantity": 140, "Unit Price": 5.00},
            "Sharpners": {"Quantity": 190, "Unit Price": 1.85}
        },
        "Office Equipment": {
            "Chairs": {"Quantity": 100, "Unit Price": 130},
            "Desks": {"Quantity": 23, "Unit Price": 350.99},
            "Fax machines": {"Quantity": 23, "Unit Price": 400},
            "Calculators": {"Quantity": 15, "Unit Price": 124.89}
        },
        "Computer Accessories": {
            "Flash Drives": {"Quantity": 87, "Unit Price": 54.88},
            "External Hard Drives": {"Quantity": 15, "Unit Price": 174.89},
            "External DVD Drives": {"Quantity": 15, "Unit Price": 84.29}
        }
    }

    desk_list, office_list, com_list = [], [], []

    choice = 0
    while choice != 5:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f'\n{"Category":<30}{"Item":<25}{"Quantity":<15}{"Unit Price"}')
            print("-" * 80)
            for cat, v in inventory.items():
                for sub, content in v.items():
                    print(f'{cat:<30}{sub:<25}{content["Quantity"]:<15}${content["Unit Price"]:.2f}')

            desk_list, office_list, com_list = create_instance(inventory)
            write_instance(desk_list, "Desk Supplies")
            write_instance(office_list, "Office Equipment")
            write_instance(com_list, "Computer Accessories")

        elif choice == 2:
            desk_list, office_list, com_list = create_instance(inventory)
            category_name = input("Enter category: ")
            if category_name == "Desk Supplies":
                category(desk_list)
            elif category_name == "Office Equipment":
                category(office_list)
            elif category_name == "Computer Accessories":
                category(com_list)
            else:
                print("Invalid category!")

        elif choice == 3:
            desk_list, office_list, com_list = create_instance(inventory)
            category_name = input("Enter category: ")
            if category_name == "Desk Supplies":
                get_item(desk_list)
            elif category_name == "Office Equipment":
                get_item(office_list)
            elif category_name == "Computer Accessories":
                get_item(com_list)
            else:
                print("Invalid category!")

        elif choice == 4:
            desk_list, office_list, com_list = create_instance(inventory)
            category_name = input("Enter category: ")
            item_name = input("Enter item name: ")
            if category_name == "Desk Supplies":
                update(desk_list, item_name)
                write_instance(desk_list, "Desk Supplies")
            elif category_name == "Office Equipment":
                update(office_list, item_name)
                write_instance(office_list, "Office Equipment")
            elif category_name == "Computer Accessories":
                update(com_list, item_name)
                write_instance(com_list, "Computer Accessories")
            else:
                print("Invalid category!")

        elif choice == 5:
            print("Program terminating...")
        else:
            print("Invalid entry!")

if __name__ == "__main__":
    main()

