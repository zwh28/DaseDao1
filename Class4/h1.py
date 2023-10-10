def sushu(a):
    t=int(pow(a,0.5))
    for i in range(1,t):
        if(a%t==0):
            return 1
    return 0
x=int(input())
b=sushu(x)
if(b==1):
    print("no")
else:
    print("yes")