x=eval(input("请输入你的成绩："))
if x<60:
    print("不合格")
elif x>=60 and x<74:
    print("合格")
elif x>=74 and x<89:
    print("良好")
else:
    print("优秀")
