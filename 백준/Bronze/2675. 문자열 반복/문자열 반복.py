a=int(input())
d=[]
d1=[]
for i in range(a):
    d=[]
    d1=[]
    b,c =input().split()
    for j in range(len(c)):
        d.append(c[j]*int(b))
        d1=d[0]
    for j in range(1,len(c)):
        d1=d1+d[j]
    print(d1)