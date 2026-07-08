import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ishu",
    database="vehicle_rental_system"
)

cursor = conn.cursor()

print("Connected to MySQL successfully!")