import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="test_db"
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
conn.commit()
conn.close()
