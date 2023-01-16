import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("Database Connected")

cursor = connection.cursor()
cursor.execute('Select * FROM Garden')
Garden = cursor.fetchall()
connection.close()

print(Garden)