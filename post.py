import sys
import os
import cgi
import cgitb
import bleach
import glob

import Page
import Sql
import RandomString

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

random_string = RandomString.RandomString(16)
dogtag = random_string.get_random_string()

pg = Page.Page(space='<P>書き込みました</P>')

form    = cgi.FieldStorage()
value   = form.getvalue('text')
cvalue  = bleach.clean(value)
dbname  = form.getvalue('dbname')
if glob.glob(f'./db/{dbname}.db'):
    db = Sql.Sql(dbname)
    db.insert(cvalue,dbname,dogtag)
    db.close()

else:
    db = Sql.Sql(dbname)
    db.table()
    db.insert(cvalue,dbname,dogtag)
    db.close()

pg.content_type()
pg.page()