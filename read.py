import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="debian-sys-maint",
  user="root",
  password="yourpassword",
  database="mydatabase"
)

with open('elements.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row[0])
        