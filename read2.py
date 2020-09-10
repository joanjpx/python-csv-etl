import csv
import mysql.connector

mydb = mysql.connector.connect(
	host="10.254.12.116",
	user="root",
	password="3x1t0s.2019",
	database="gilatssra2"
)

cursor = mydb.cursor()
rs = cursor.execute('SELECT * FROM elements')

count = rs.rowcount;

if count>0:
	for x in rows:
		print x
else:
	print "No ResultSet"
	


with open('elements.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
	print row    	
exit()

        
