print(bool(250), 
bool('假'),      
bool('False'),   
bool(False),'\n',
bool(""),        
bool(520),       
bool(0),         
bool(0.0),       
bool(0j))
if 520>250:
    print("520比250大！")
else:
    print("520不比250大！")

if bool(250):
    print("250 is True")
else:
    print("250 is False")

print(1==True, 0==False, True+False, True-False, True*False)
#print(True/False)

print(3<4 and 4<5, 
     3>4 and 4<5,  
     3<4 and 4>5,  
     3>4 and 4>5,  '\n',

     3<4 or 4<5,   
     3>4 or 4<5,   
     3<4 or 4>5,   
     3>4 or 4>5,
     "FishC" and "LOVE",
     "FishC" or 250)

     