#  Change Control test comment for SQA demonstration

products = {}  # Dictionary to store products
next_id = 1  # ID counter

def add_product():
    global next_id
    print("\n--- Add Product ---")
    name = input("Enter product name: ")
    while True:
        try:
            price = float(input("Enter product price: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")
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
         print(f"Total products: {len(products)}")
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



def menu():
    while True:
        print("\n=== Admin Panel Menu ===")
        print("1. Add Product")
        print("2. List Products")
        print("3. Delete Product")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            print(" Exiting...")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    menu()
