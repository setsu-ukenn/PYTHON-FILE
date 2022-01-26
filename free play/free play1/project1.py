import sys   
sys.setrecursionlimit(100000)
i=1
y=1
def layer(int):
    if(i<15):
        y=i+math.pow( layer(i+1),(1.0/(i+1)) )
        print("%10.3f" % y)
        return y
layer(1)
print("%10.3f" % y)
