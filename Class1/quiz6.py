a=input().split(" ")
for i in range(4):
    for j in range(i+1,4):
        if(a[i]<a[j]):
            d=a[i]
            a[i]=a[j]
            a[j]=d
print(a)