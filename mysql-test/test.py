import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passw0rd",
    database="liverpooltest"
)

mycurser = db.cursor()

# mycurser.execute("CREATE DATABASE liverpooltest")
