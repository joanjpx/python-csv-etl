import csv
from Database import Database

with open('elements.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row[1])
        m = Database()
        m.selectOne(row[1])
    	
    	

		  	


        
