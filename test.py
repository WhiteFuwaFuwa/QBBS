import os
import Sql

def Muda(a,b,c):
    return print(a,b,c)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
import Search
s = Search.Search('front','SheNrhMTriUfoVrs')
print('Content-Type: text/html\n')
print(s.search())
ss = s.search()
print(ss)
Muda(ss[0][0],ss[0][1],ss[0][2])
SQL = Sql.Sql('core')
print(SQL.view)
SQL.close()
s.close()