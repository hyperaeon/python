__author__ = 'hzliyong'
import re
phone = '2004-959-559 # This is Phone Number'

#Delete python-style comments
num = re.sub(r'#.*$',"",phone)
print("Phone number:",num)

#Remove any other than digits
num = re.sub(r'\D',"",phone)
print("Phone number:",num)
