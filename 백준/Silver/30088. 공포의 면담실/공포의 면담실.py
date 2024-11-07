a=int(input())
c=[]
d=[]

for i in range(a):
    b=list(map(int,input().split()))
    c.append(b)
    b=sum(c[i][1:c[i][0]+1])
    d.append(b)
d.sort()

sum=0
for i in range(a):
    sum=sum+d[i]*(a-i)
print(sum)