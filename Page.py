class Page:
    def __init__(self,form = False, action = 'example.py',dbname = 'front', space = ''):
        self.form   = form
        self.action = action
        self.dbname = dbname
        self.space  = space
        self.branches = ''
    
    def content_type(self):
        return print("Content-Type: text/html\n")
    
    def current(self,branch):
        for i in branch:
            self.branches += f'<li><a href="../{i[1]}/{i[2]}">{i[0]}</a></li>'
        return self.branches
    
    def free(self):
        return self.space
    
    def make_form(self):
        if self.form == True:
            form = f'''        <div>
                <form action = "../../{self.action}" method = "POST">
                    <input type = "text" name = "text">
                    <input type = "submit" value = "投稿">
                    <input type = "hidden" value = "{self.dbname}" name = "dbname">
                </form>
            </div>
    '''
        else:
            form = ''
        return form

    def page(self):
        html = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Q</title>
    </head>
    <body>
        {self.make_form()}
        {self.free()}
        {self.branches}
    </body>
</html>
'''
        return print(html)