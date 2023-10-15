arr = list(input("请输入一个数组\n").split(" "))
length=len(arr)
b=[1 for i in range (0,length)]
for i in range(0,length):
    for j in range(0,length):
        if(i!=j):
            b[i]*=int(arr[j])
print(arr)
print(b)