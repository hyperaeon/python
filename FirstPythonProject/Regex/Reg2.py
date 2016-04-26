__author__ = 'hzliyong'

import re
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*)are (.*?) .*',line,re.M |re.I)

if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else :
    print("No match!")

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())