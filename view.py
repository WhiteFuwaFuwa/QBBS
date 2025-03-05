import sys
import os
import cgitb
import glob
import re

import Page
import Sql
import Search

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

get_path = os.environ.get('PATH_INFO')
row_keys = re.findall('/[a-zA-Z]+',get_path)
keys = []
for i in row_keys:
    keys.append(i.replace('/',''))
if len(keys) >= 2:
    if glob.glob(f'./db/{keys[1]}.db'):
        db = Sql.Sql(keys[1])
    else:
        search = Search.Search(keys[0],keys[1])
        child  = search.search()
        db     = Sql.Sql(keys[1])
        db.table()
        db.insert(child[0][0],child[0][1],child[0][2])    
        search.close
    page   = Page.Page(True, 'post.py',keys[1])
else:
    if glob.glob(f'./db/front.db'):
        db = Sql.Sql('front.db')
    else:
        pass
    page   = Page.Page(True, 'post.py','front')
current = db.view()
page.current(current)
db.close()


page.content_type()
page.page()