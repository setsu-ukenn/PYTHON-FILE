i=1
def layer(int):
    if i< 15:
        y=i+pow(layer(i+1),(1.0/(i+1)))
    return y
layer(1)
print(".20lf" % y)


