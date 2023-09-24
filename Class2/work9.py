import math
import random
def hanshu(x):
    result=x**2+4*x*math.sin(x)
    return result
n=int(input("请输入次数:"))
sum=0
for i in range(n):
    x=random.uniform(2,3)
    sum+=hanshu(x)
result=sum/n
print("%.6f"%result)