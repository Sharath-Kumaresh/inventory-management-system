import mysql.connector

# Connect to MySQL database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="262009",
        database="student_db"
    )

def add_item():
    name = input("Enter Item Name: ")
    price = int(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))
    
    db = get_connection()
    cursor = db.cursor()
    
    query = "INSERT INTO inventory (item_name, price, quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, price, qty))
    
    db.commit() 
    print(f"✅ '{name}' successfully added to database!")
    db.close()

def view_items():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory")
    
    print("\n--- Current Inventory Records ---")
    rows = cursor.fetchall()
    if not rows:
        print("No items found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Item: {row[1]} | Price: ₹{row[2]} | Quantity: {row[3]}")
    print("---------------------------------\n")
    db.close()

def delete_item():
    view_items()
    item_id = int(input("Enter the ID of the item to delete: "))
    
    db = get_connection()
    cursor = db.cursor()
    
    query = "DELETE FROM inventory WHERE id = %s"
    cursor.execute(query, (item_id,))
    
    db.commit()
    print("Item with ID {item_id} deleted successfully!")
    db.close()
while True:
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. View Inventory")
    print("2. Add New Item")
    print("3. Delete Item")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        view_items()
    elif choice == '2':
        add_item()
    elif choice == '3':
        delete_item()
    elif choice == '4':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, please select 1-4.")
