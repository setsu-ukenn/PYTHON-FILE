print([1,2,3,4,5],[1,2,3,4,5,"上山打老虎"])
rhyme=[1,2,3,4,5,"上山打老虎"]
print(rhyme)
for each in rhyme:
    print(each)
print(rhyme[0],rhyme[1],rhyme[5])

length=len(rhyme)
rhyme[length-1]
rhyme[-1]

print(rhyme[0:3],rhyme[3:6],rhyme[:3],rhyme[3:],rhyme[:],rhyme[0:6:2])
print(rhyme[::2],rhyme[::-2],rhyme[::-1])

