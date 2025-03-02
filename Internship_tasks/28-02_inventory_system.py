
title = "Welcome to Simple Inventory Management System"
print(title.center(100))
print("\n")
print("-"*150)

inventory = {
    "product_id": [101,102,103,104,105],
    "name": ["Rice","Wheat","Sugar","Jowar","Oil"],
    "price": [70,55.5,43,110,130.9],
    "stock": [55,45,30,35,15]
}

while True:
    print("\n1. Add a New Product\n2. Update stock for an Existing product\n3. Sell a Product\n4. Display Inventory\n5. Exit the system")
    choice = int(input("Enter an Inventory Action: "))
    
    
    if choice == 1:
        p_id = int(input("Enter Product ID: "))
        
        for product_id, entry in inventory.items():
            if p_id in entry:
                print("Product ID already exists. Please enter a different ID.")
            else:
                name = str(input("Enter Product Name: "))
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Product Stock: "))
                inventory["product_id"].append(p_id)
                inventory["name"].append(name)
                inventory["price"].append(price)
                inventory["stock"].append(stock)
                print(f"Product ID: {p_id} ")
                print(f"Product Name: {name} ")
                print(f"Product Price: {price} ")
                print(f"Product Stock: {stock} ")
            break
    
    elif choice == 2:
        select_product = int(input("Enter Product ID to Update: "))
        for product_id, entry in inventory.items():
            if select_product not in entry:
                print("Product ID does not exist in inventory!")
                break
            else:
                update_stock = int(input("Enter New Stock: "))
                inventory["stock"][inventory["product_id"].index(select_product)] = update_stock
                print(f"Stock for Product ID {select_product} has been updated to {update_stock}")
                print(f"Product ID: {select_product} ")
                print(f"Stock: {update_stock} ")
                break
    
    elif choice == 3:
        select_product = int(input("Enter Product ID to sell: "))
        for product_id, entry in inventory.items():
            if select_product not in entry:
                print("Product ID does not exist in inventory!")
                break
            else:
                select_stock = int(input("Enter Quantity to sell: "))
                if select_stock > inventory["stock"][inventory["product_id"].index(select_product)]:
                    print("Not enough stock to sell!")
                    break
                else:
                    rem_stock = inventory["stock"][inventory["product_id"].index(select_product)] - select_stock
                    print(f"Product ID: {select_product} ")
                    print(f"Quantity sold: {select_stock} ")
                    print(f"Stock remaining: {rem_stock}")
                    inventory["stock"][inventory["product_id"].index(select_product)] = rem_stock
                    break
    
    elif choice == 4:
        print("Inventory")
        for i in range(len(inventory["product_id"])):
                print(f"Product ID: {inventory['product_id'][i]}, Name: {inventory['name'][i]}, Price: {inventory['price'][i]}, Stock: {inventory['stock'][i]}")
    
    elif choice == 5:
        print("Exiting the Simple Inventory System")
        print("Thank you !!")
        break
    
    else:
        print("Invalid choice. Please choose a valid option.")
                    
    
        