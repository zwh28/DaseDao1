x=int(input())
y=int(input())
min=0
if x>y:
    min=y
else:
    min=x
gong=0
for i in range(1,min+1):
    if x%i==0 and y%i==0:
        gong=i
print("最大公约数是：%d"%gong)

