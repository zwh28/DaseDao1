a=input().split(" ")
l=len(a)
for i in range(l):
    for j in range(i+1,l):
        if(a[i]<a[j]):
            d=a[i]
            a[i]=a[j]
            a[j]=d
print(a)

b=input().split(" ")
