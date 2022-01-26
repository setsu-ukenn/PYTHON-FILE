if 3>5:
    print("我在里面")
    print("我也在里面")
print("我在外面")

if "小甲鱼"=="小姐姐":
    print("小甲鱼是小姐姐！")
else:
    print("小甲鱼不是小姐姐！")

score=input("请输入你的分数:")
score=float(score)

if 0<=score<=100:
    if 0<=score<60:
        print("D")
    elif score<80:
        print("C")
    elif score<90:
        print("B")
    elif score<100:
        print("A")
    else: print("S")
else: print("输入错误")


