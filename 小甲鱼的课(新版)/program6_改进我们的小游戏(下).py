"""用python设计第一个游戏"""
import random

counts=3
answer=random.randint(1,10)

while counts>0:
    temp=input("不妨猜一下小甲鱼现在心里想的是哪个数字")
    guess=int(temp)
    
    if guess==answer:
        print("你是小甲鱼心里的蛔虫吗?!")
        print("哼，猜中了也没奖励!")
        break
    else:
        if guess<answer:
            print("小啦...")
        else:
            print("大啦...")
    counts=counts-1

print("游戏结束，不玩啦^_^")


#攻击伪随机数
x=random.getstate()
print(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))

random.setstate(x)
print(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))



