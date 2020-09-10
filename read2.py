import csv
import mysql.connector

mydb = mysql.connector.connect(
	host="10.254.12.116",
	user="root",
	password="3x1t0s.2019",
	database="gilatssra2"
)


with open('elements20200910.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
    	c = mydb.cursor(buffered=True)
    	sql = "SELECT * FROM elements WHERE identifier='"+row[3]+"'"
    	#print sql
    	query = c.execute(sql)

    	if(hasattr(query,"fetchall")):
    		row = query.fetchall()
    		print sql
    	else:
    		continue
    	

		  	


        
