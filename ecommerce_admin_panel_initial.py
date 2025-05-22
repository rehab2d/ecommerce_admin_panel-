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
