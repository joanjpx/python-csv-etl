import csv
from Database import Database

with open('elements.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
        #print(row[1])
        m = Database()
        rID = m.selectOne(row[1])
        if rID!=False:
            m.updateRow(rID,row[3])
        else:
            print("No Match")
            
            
    	
    	

		  	


        
