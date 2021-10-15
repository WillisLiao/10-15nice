import random as rand

n= rand.randint(1,99)
a= int(input())
count=0
while a!= n:
    
    if a>n:
        count+=1
        print("smaller")
        a=int(input())
        
    elif a<n:
        count+=1
        print("bigger")
        a=int(input())
        
    else:
        break
print("猜對了是",n,"猜了",count,"次")
    
