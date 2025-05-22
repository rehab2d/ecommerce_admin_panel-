products = {}  # Dictionary to store products
next_id = 1  # ID counter

def add_product():
    global next_id
    print("\n--- Add Product ---")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    product = {
        "name": name,
        "price": price
    }
    products[next_id] = product
    print(f"Product '{name}' added with ID {next_id}")
    next_id += 1

def list_products():
    print("\n--- Product List ---")
    if not products:
        print("No products found.")
    else:
        for pid, prod in products.items():
            print(f"ID: {pid} | Name: {prod['name']} | Price: {prod['price']}")


def delete_product():
    print("\n--- Delete Product ---")
    try:
        pid = int(input("Enter product ID to delete: "))
        if pid in products:
            del products[pid]
            print("Product deleted.")
        else:
            print(" Product ID not found.")
    except ValueError:
        print("Invalid ID format.")
