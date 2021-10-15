v1=0
a=0
n=int(input())
for i in range(n):
    v1+=1
    a=a+(v1*(v1+1))
print(a)