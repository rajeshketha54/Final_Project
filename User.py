class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []
        self.selected_items = []

    def place_new_order(self, restaurant_menu):
        print("Menu:")
        for index in range(len(restaurant_menu)):
            print(f"{index + 1}. {restaurant_menu[index]}")

        selected_indices = input("Select the food items by entering the corresponding numbers (comma-separated): ")
        selected_indices = [int(index) for index in selected_indices.split(",")]

        self.selected_items = [restaurant_menu[index - 1] for index in selected_indices]

        print("Selected Items:")
        for item in self.selected_items:
            print(item)

        place_order = input("Place the order? (yes/no): ")
        if place_order.lower() == "yes":
            self.order_history.append(self.selected_items)
            self.selected_items = []
            print("Order placed successfully!")
        else:
            print("Order cancelled.")

    def view_order_history(self):
        if self.order_history:
            print("Order History:")
            for order_index in range(len(self.order_history)):
                print(f"Order {order_index + 1}:")
                for item in self.order_history[order_index]:
                    print(item)
                print("------------------------")
        else:
            print("No order history.")

    def update_profile(self):
        print("Update Profile:")
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email address: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter your password: ")

def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    return User(full_name, phone_number, email, address, password)

restaurant_menu = [
    "Tandoori Chicken (4 pieces) [INR 240]",
    "Vegan Burger (1 Piece) [INR 320]",
    "Truffle Cake (500gm) [INR 900]"
]
print("Welcome to the Application!")
user = None
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user = register_user()
        print("Registration successful!")
        continue  # Go back to the choice selection
    elif choice == "2":
        if user is None:
            print("Please register to use the application.")
        else:
            print("Login")
            email = input("Enter your email address: ")
            password = input("Enter your password: ")
            if user.email == email and user.password == password:
                print("Login successful!")
                break
            else:
                print("Invalid email or password. Please try again.")
    elif choice == "3":
        break
    else:
        print("\nInvalid choice. Please try again.")

if user is not None:
    while True:
        print("\nOptions:")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user.place_new_order(restaurant_menu)
        elif choice == "2":
            user.view_order_history()
        elif choice == "3":
            user.update_profile()
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.")
print("Thank you for using the application!")
