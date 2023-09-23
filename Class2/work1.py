def find_max(n):
    y=n % 3
    ge=int(n / 3)
    result=[]
    if(y==0):
        for i in range(ge):
            result.append(3)
    elif(y==1):
        result.append(2)
        result.append(2)
        for i in range(ge-1):
            result.append(3)
    else:
        result.append(2)
        for i in range(ge):
            result.append(3)
    return result
n=int(input())
r=find_max(n)
print(r)