i=0
while i<len("FishC"):
    print("FishC"[i],end=" ")
    i +=1
print("\n")

for i in range(10):
    print(i,end=" ")
print("\n")

for i in range(5,10):
    print(i,end=" ")
print("\n")

for i in range(5,10,2):
    print(i,end=" ")
print("\n")

for i in range(10,5,-2):
    print(i,end=" ")
print("\n")

sum=0
for i in range(1000001):
    sum+=i
print(sum,"\n")

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x, "*", n//x)
            break
    else:
        print(n,"是一个素数")