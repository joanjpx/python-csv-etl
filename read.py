import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="django"
)

with open('elements.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row[0])
        