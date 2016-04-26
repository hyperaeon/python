__author__ = 'hzliyong'
import cgi,os
import cgitb;
cgitb.enable()

form = cgi.FiledStorage()

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('/temp/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file ' + fn + '"was uploaded successfully'

else:
    message = 'No file was uploded'

print('''
    Content-type:text/hteml\n
    <html>
    <body>
        <p>%s</p>
    </body>
    </html>
    ''')% (message)