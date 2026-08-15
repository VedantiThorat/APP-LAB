# Mobile Store Management System

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def categorize(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand    :", self.brand)
        print("Model    :", self.model)
        print("Price    :", self.price)
        print("Category :", self.categorize())
        print("------------------------")


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all(self):
        if len(self.mobiles) == 0:
            print("No mobiles available.")
        else:
            print("\n===== MOBILE STORE =====")
            for mobile in self.mobiles:
                mobile.display()


# Create Store object
store = Store()

while True:
    print("\n1. Add Mobiles")
    print("2. Display All Mobiles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        # Ask how many mobiles to add
        n = int(input("How many mobiles do you want to add? "))

        for i in range(n):
            print("\nEnter details of Mobile", i + 1)

            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            price = float(input("Enter Price: "))

            mobile = Mobile(brand, model, price)
            store.add_mobile(mobile)

        print("\nAll mobiles added successfully!")

    elif choice == 2:
        store.display_all()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")