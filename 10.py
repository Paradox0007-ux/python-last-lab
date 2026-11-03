
store1 = {
    "Laptop": 10,
    "Mobile": 20,
    "Keyboard": 15,
    "Mouse": 30
}

store2 = {
    "Laptop": 5,
    "Mobile": 12,
    "Monitor": 8,
    "Mouse": 10
}

store3 = {
    "Laptop": 7,
    "Keyboard": 10,
    "Monitor": 5,
    "Printer": 6
}


while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Display Store Inventory")
    print("2. Search Product")
    print("3. Add or Update Stock")
    print("4. Merge All Store Inventories")
    print("5. Calculate Total Stock")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStore 1:", store1)
        print("Store 2:", store2)
        print("Store 3:", store3)

    elif choice == "2":
        product = input("Enter product name: ")

        print("\nProduct:", product)
        print("Store 1:", store1.get(product, 0))
        print("Store 2:", store2.get(product, 0))
        print("Store 3:", store3.get(product, 0))

        if product not in store1 and product not in store2 and product not in store3:
            print("Product not found in any store!")

    elif choice == "3":
        store_no = input("Enter store number (1/2/3): ")
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))

        if quantity < 0:
            print("Quantity cannot be negative!")

        elif store_no == "1":
            store1[product] = store1.get(product, 0) + quantity
            print("Store 1 inventory updated!")

        elif store_no == "2":
            store2[product] = store2.get(product, 0) + quantity
            print("Store 2 inventory updated!")

        elif store_no == "3":
            store3[product] = store3.get(product, 0) + quantity
            print("Store 3 inventory updated!")

        else:
            print("Invalid store number!")

    elif choice == "4":
        merged = {}

        for store in (store1, store2, store3):
            merged.update(store)

        print("\nMerged Inventory:", merged)

        total_inventory = {
            product: store1.get(product, 0)
            + store2.get(product, 0)
            + store3.get(product, 0)
            for product in set(store1) | set(store2) | set(store3)
        }

        print("Combined Stock:", total_inventory)

    elif choice == "5":
        total = sum(store1.values()) + sum(store2.values()) + sum(store3.values())

        print("Total Stock Across All Stores:", total)

    elif choice == "6":
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid choice! Try again.")
