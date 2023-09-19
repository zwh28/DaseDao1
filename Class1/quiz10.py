a=input()
l=len(a)
s=0
for i in range(l-1):
    if(a[i]==a[i+1]):
        s=1
if(s==0):
    print("no")
else:
    print("yes")