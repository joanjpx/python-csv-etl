import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="10.254.12.116",
            user='root',
            password='3x1t0s.2019',
            db='gilatssra2'
        )
        
        self.cursor = self.connection.cursor()
        
    def selectOne(self, identifier):
        sql = "SELECT * FROM elements WHERE identifier='{id}'".format(id=identifier)
        print(sql)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            print(row[2])
        except Exception as e:
            print("No Resultset")
            #raise     
    
    def updateRow(self, identifier, platform):
        sql = "SELECT * FROM elements WHERE identifier='{id}'".format(id=identifier)
        print(sql)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            print(row[2])
        except Exception as e:
            print("No Resultset")
            #raise     

#database = Database()
#database.selectOne("HC-0002-CS01")
#database.selectOne("HC-0004-CO01")