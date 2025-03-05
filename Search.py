import os
import sqlite3
import glob

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Search:
    def __init__(self,mother,child):
        self.mother = mother
        self.child  = child
    def search(self):
        self.connect = sqlite3.connect('./db/' + self.mother + '.db')
        self.cursor   = self.connect.cursor()
        self.cursor.execute('SELECT * FROM branch WHERE fork = ?',(self.child,))
        tuple = self.cursor.fetchall()
        return tuple
    def close(self):
        self.cursor.close()
        self.connect.close()