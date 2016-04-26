__author__ = 'hzliyong'

template = '''<html>
    <head><title>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>'''
data = {'title': 'My home page', 'text' : 'Welcome to my page'}
print(template % data)