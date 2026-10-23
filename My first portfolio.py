import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="262009",
    database="student_db")
cursor = db.cursor()
cursor.execute("SELECT * FROM inventory")
print("--- Current Database Records ---")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Item: {row[1]} | Price: {row[2]} | Qty: {row[3]}")
db.close()
