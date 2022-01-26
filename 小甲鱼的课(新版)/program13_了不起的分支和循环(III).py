#while condition:
#    statement(s)

love="yes"
while love =="yes":
    love=input("今天你还爱我吗?")

i=1
sum=0
while i<=1000000:
    sum+=i
    i +=1
print(sum)

#while True:
#    print("作为一段没有灵魂的代码，我的任务就是不断的干活！")

while True:
    answer=input("主人，我可以退出循环了吗?")
    if answer =="可以":
        break
    print("哎,好累~~")