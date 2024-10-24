a,b=list(input().split())
c=[]
d=[]
c1=[]
d1=[]

for j in range(len(a)):
    c.append(a[len(a)-1-j])
    d.append(b[len(b)-1-j])

c1=c[0]
d1=d[0]
for j in range(1,len(a)):
    c1=c1+c[j]
    d1=d1+d[j]

if c1>d1:
    print(c1)
else:
    print(d1)