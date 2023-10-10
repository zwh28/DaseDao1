x=float(input())
y=int(x)
xiao=x-y
erzheng=bin(y)
print(erzheng, end='')
print('.', end='')
c=0.5
while(abs(xiao)>0.0000000000001):
    if xiao>=c:
        print(1, end='')
        xiao -= c
        c = c / 2
    else:
        print(0, end='')
        c =c / 2
