v1=1
v2=1
a=0
n=int(input())
for i in range(n):
    a=a+(1/(v1*(v2+1)))
    v2+=1
    v1, v2= v2, v1+v2
print(a)