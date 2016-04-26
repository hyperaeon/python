__author__ = 'hzliyong'

phonebook = {'Beth': '9102', 'Alice': '3902', 'Cecil': '9099'}
print("Cecil's phone number is %(Cecil)s." % phonebook)

template = '''<html>
    <head><titel>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>'''
data = {'title':'My Home Page','text':'Welcome to my home page'}
print(template % data)
