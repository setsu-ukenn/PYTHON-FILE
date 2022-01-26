heros=["钢铁侠","绿巨人"]
heros.append("黑寡妇")
heros.extend(["鹰眼","灭霸","雷神"])
print(heros)
s=[1,2,3,4,5]
s[len(s):]=[6]
s[len(s):]=[7,8,9]
print(s)

s=[1,3,4,5]
print(s)
s.insert(1,2)
print(s)
s.insert(0,0)
print(s)
s.insert(len(s),6)
print(s)

heros.remove("灭霸")
#heros.remove("金莲")
print(heros.pop(2))
print(heros)
heros.clear()
print(heros)