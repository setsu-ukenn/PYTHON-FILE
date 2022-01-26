i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)
    
    
i=1
while i<5:
    print("循环内,i的值是",i)
    i+=1
else:
    print("循环外,i的值是",i)
    
    
day=1
while day <=7:
    answer=input("今天有好好学习吗?")
    if answer !="有":
        break
    day+=1
else:
    print("非常棒,你已经坚持了7天连续学习!")
    

i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,"=",j*i,end=" ")
        j+=1
    print()
    i+=1
    

day=1
hour=1
while day<=7:
    while hour<=8:
        print("今天我一定要坚持学习8个小时!")
        hour+=1
        if hour>1:
            break
    day+=1