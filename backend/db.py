import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@thouhid243427",
    database="canteen_db"
)

cursor = db.cursor()