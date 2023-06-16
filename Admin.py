class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Restaurant:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("\nFood item added successfully!")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("\nFood item updated successfully!")
                return
        print("\nFood item not found.")

    def view_food_items(self):
        if self.food_items:
            print("Food Items:")
            for food_item in self.food_items:
                print(f"\tFood ID: {food_item.food_id}")
                print(f"\tName: {food_item.name}")
                print(f"\tQuantity: {food_item.quantity}")
                print(f"\tPrice: {food_item.price}")
                print(f"\tDiscount: {food_item.discount}")
                print(f"\tStock: {food_item.stock}")
                print("\t------------------------")
        else:
            print("\nNo food items available.")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("\nFood item removed successfully!")
                return
        print("\nFood item not found.")

restaurant = Restaurant()

while True:
    print("\n-------- Welcome to the Restaurant Management System --------\n")
    print("1. Add new food item")
    print("2. Edit food item")
    print("3. View food items")
    print("4. Remove food item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = input("Enter the price of the food item: ")
        discount = input("Enter the discount of the food item: ")
        stock = input("Enter the stock of the food item: ")
        restaurant.add_food_item(name, quantity, price, discount, stock)
    elif choice == "2":
        food_id = input("\nEnter the Food ID of the item you want to edit: ")
        name = input("Enter the new name: ")
        quantity = input("Enter the new quantity: ")
        price = input("Enter the new price: ")
        discount = input("Enter the new discount: ")
        stock = input("Enter the new stock: ")
        restaurant.edit_food_item(int(food_id), name, quantity, price, discount, stock)
    elif choice == "3":
        restaurant.view_food_items()
    elif choice == "4":
        food_id = input("\nEnter the Food ID of the item you want to remove: ")
        restaurant.remove_food_item(int(food_id))
    elif choice == "5":
        print("\nThank you for using the Restaurant Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
