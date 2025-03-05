import sqlite3

class Sql:
    def __init__(self,database='front'):
        self.database = database
        self.connect = sqlite3.connect('./db/' + database + '.db')
        self.cursor  = self.connect.cursor()
    
    def table(self):
        self.cursor.execute('CREATE TABLE branch(text STRING, origin STRING, fork STRING)')
        self.connect.commit()

    def insert(self,text, origin, fork):
        self.cursor.execute('INSERT INTO branch(text, origin, fork) values(?, ?, ?)', (text, origin, fork))
        self.connect.commit()

    def view(self):
        self.cursor.execute('SELECT * FROM branch')
        return self.cursor.fetchall()
    
#    def search(self,next_database):
#        self.cursor.execute('SELECT * FROM branch WHERE fork = ?',(next_database,))
    
    def close(self):
        self.cursor.close()
        self.connect.close()