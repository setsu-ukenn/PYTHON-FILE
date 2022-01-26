heros=["蜘蛛侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
heros[4]="钢铁侠"
print(heros)
heros[3:]=["武松","林冲","李逵"]

nums=[3,1,9,6,8,3,5,3]
nums.sort()
print(nums)
nums.reverse()
print(nums)
heros.reverse()
print(heros)
nums=[3,1,9,6,8,3,5,3]
nums.sort(reverse=True)
print(nums)

print(nums.count(3))
heros[heros.index("绿巨人")]="神奇女侠"
print(heros)

nums=[3,1,9,6,8,3,5,3]
nums.index(3)
nums.index(3,1,7)
nums_copy1=nums.copy()
nums_copy2=nums[:]
print(nums_copy1,nums_copy2)

