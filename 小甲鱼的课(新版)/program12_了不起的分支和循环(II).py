age=16
if age<18:
    print("抱歉，未满18岁禁止访问。")
else:
    print("欢迎您来^o^")


print("抱歉，未满18岁禁止访问。")if age<18 else print("欢迎您来^o^")

score=66
level=('D' if 0<=score<60 else
       'C' if 60<=score< 80 else
       'B' if 80<=score<90 else
       'A' if 90<=score<100 else
       'S' if score==100 else
       "请输入 0-100 之间的分值^o^")
print(level)

age=18
isMale=True
if age<18:
    print("抱歉，未满18岁禁止访问。")
else:
    if isMale:
        print("任君选购！")
    else:
        print("抱歉，本店商品可能不适合小公举哦~")