import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan_visual"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT name FROM kategori')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)