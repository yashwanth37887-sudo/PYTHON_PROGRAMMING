
# Integrated E-Commerce Order Processing
# and Reconciliation System

# Initial Product Inventory
products = {
    101: {
        "name": "Laptop",
        "price": 50000,
        "stock": 20
    },
    102: {
        "name": "Mobile",
        "price": 20000,
        "stock": 30
    },
    103: {
        "name": "Headphones",
        "price": 2000,
        "stock": 50
    }
}

# Store order and inventory information
orders = []
total_revenue = 0

# Display products
def display_products():
    print("\nAVAILABLE PRODUCTS")
    print("-" * 55)

    for pid, item in products.items():
        print(
            f"ID: {pid} | "
            f"Name: {item['name']} | "
            f"Price: Rs.{item['price']} | "
            f"Stock: {item['stock']}"
        )

# Process customer orders
def process_order():
    global total_revenue

    display_products()

    pid = int(input("\nEnter Product ID: "))
    quantity = int(input("Enter Order Quantity: "))

    if pid not in products or quantity <= 0:
        print("Invalid product or quantity!")
        return

    if quantity > products[pid]["stock"]:
        print("Insufficient stock!")
        return

    discount = float(input("Enter Discount (%): "))

    if discount < 0 or discount > 100:
        print("Invalid discount!")
        return

    item = products[pid]

    amount = item["price"] * quantity
    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount

    # Dispatch products
    products[pid]["stock"] -= quantity

    # Update revenue
    total_revenue += final_amount

    orders.append({
        "product_id": pid,
        "quantity": quantity,
        "amount": final_amount,
        "discount": discount
    })

    print("\nORDER SUCCESSFUL")
    print("Product:", item["name"])
    print("Total Amount: Rs.", amount)
    print("Discount: Rs.", discount_amount)
    print("Final Amount: Rs.", final_amount)
    print("Dispatch Quantity:", quantity)

# Process product returns
def process_return():
    display_products()

    pid = int(input("\nEnter Product ID for Return: "))
    quantity = int(input("Enter Return Quantity: "))

    if pid not in products or quantity <= 0:
        print("Invalid return details!")
        return

    # Calculate quantity previously dispatched
    dispatched = sum(
        order["quantity"]
        for order in orders
        if order["product_id"] == pid
    )

    # Calculate quantity already returned
    returned = products[pid].get("returned", 0)

    if quantity > dispatched - returned:
        print("Return quantity exceeds dispatched quantity!")
        return

    # Update inventory
    products[pid]["stock"] += quantity
    products[pid]["returned"] = returned + quantity

    print("\nRETURN SUCCESSFUL")
    print("Product:", products[pid]["name"])
    print("Returned Quantity:", quantity)
    print("Updated Stock:", products[pid]["stock"])

# Generate final inventory report
def inventory_report():
    print("\n========== FINAL INVENTORY REPORT ==========")

    print(
        f"{'ID':<8}{'Product':<15}"
        f"{'Initial':<10}{'Sold':<10}"
        f"{'Returned':<10}{'Final':<10}"
    )

    print("-" * 65)

    for pid, item in products.items():

        sold = sum(
            order["quantity"]
            for order in orders
            if order["product_id"] == pid
        )

        returned = item.get("returned", 0)

        initial = item["stock"] + sold - returned

        expected_stock = initial - sold + returned

        actual_stock = item["stock"]

        discrepancy = expected_stock - actual_stock

        print(
            f"{pid:<8}{item['name']:<15}"
            f"{initial:<10}{sold:<10}"
            f"{returned:<10}{actual_stock:<10}"
        )

        if discrepancy != 0:
            print("Stock Discrepancy:", discrepancy)
        else:
            print("Stock Status: Matched")

    print("-" * 65)
    print("Total Orders:", len(orders))
    print("Total Revenue: Rs.", round(total_revenue, 2))
    print("============================================")

# Main program
while True:

    print("\n===== E-COMMERCE MANAGEMENT SYSTEM =====")
    print("1. Display Products")
    print("2. Process Order")
    print("3. Process Return")
    print("4. Inventory Report")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        process_order()

    elif choice == "3":
        process_return()

    elif choice == "4":
        inventory_report()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid Choice! Try Again.")

