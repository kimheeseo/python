a=int(input())
c=[]

for i in range(a):
    d=int(input())
    c.append(d)
#print(c)
c.sort()

for i in range(a):
  print(c[i])