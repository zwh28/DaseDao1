import re
id_number=input()
pattern='(^\d{15}$)|(^\d{17}([0-9]|X)$)'
x=re.match('(^\d{15}$)|(^\d{17}([0-9]|X)$)',id_number)
if x:
    print('true')
else:
    print('false')