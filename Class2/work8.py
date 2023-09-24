#第一种级数方法
def count_pi():
    n=10000000
    sum=0
    for i in range(n):
        if(i % 2 ==0):
            sum+=1/(2*i+1)
        else:
            sum-=1/(2*i+1)
    sum=sum*4
    print("%.10f"%sum)
count_pi()

#第二种级数方法
pi = 0
N = 100
for k in range(N):
    pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
print("%.10f"%pi)

#第三种方法  蒙特卡洛法
import random
dot=0
dots=int(input())
for i in range(0,dots):
    x=random.random()
    y=random.random()
    r=pow(x**2+y**2,0.5)
    if(r<=1):
        dot+=1
pi=4*(dot/dots)
print("%.10f"%pi)
