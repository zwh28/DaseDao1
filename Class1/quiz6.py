a=input()
b=input()
c=input()
if a>b:
    first=a
    second=b
else:
     first=b
     second=a
if first<c:
    third=second
    second=first
    first=c
elif first>c and c>second:
    third=second
    second=c
elif c<second:
    third=c

print('first number:',third)
print('second number:',second)
print('third number:',first)
