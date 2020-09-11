import csv;
import mysql.connector;

mydb = mysql.connector.connect(
	host="10.254.12.116",
	user="root",
	password="3x1t0s.2019",
	database="gilatssra2"
)

c = mydb.cursor()
c.execute("SELECT * FROM elements")
rs = c.fetchall()

def readDocument(identifier):
    with open('elements.csv') as File:  
        reader = csv.reader(File)
        for row in reader:
            if(row[1]==identifier):
                print(row[1])
                curs = mydb.cursor()
                curs.execute("UPDATE elements SET platforms_2={platform} WHERE identifier={identifier}".format(platform=row[2],identifier=identifier))
            else:
                print("No match")
        curs.commit();
#end        
for row in rs:
    print(row[3])
    readDocument(row[3])



        
        
    	    
                
    	

		  	


        
