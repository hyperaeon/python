__author__ = 'hzliyong'

from os import environ
import cgi,cgitb

if environ.hasKey('HTTP_COOKIE'):
    for cookie in map(strip, split(environ['HTTP_COOKIE'],';')):
        (key, value) = split(cookie,'=')
        if key == 'UserID':
            user_id = value

        if key == 'Password':
            password = value

print("User ID = %s" % user_id)
print("Password = %s" % password)