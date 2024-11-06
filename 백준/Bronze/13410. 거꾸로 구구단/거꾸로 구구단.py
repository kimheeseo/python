a,b=map(int,input().split())
c=[]

for i in range(1,b+1):
  c.append(int(str(i*a)[::-1]))
max=0

for i in range(len(c)):
  if max<c[i]:
    max=c[i]
print(max)    
