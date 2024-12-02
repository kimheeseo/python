a,b=map(int, input().split())
aa,bb=map(int, input().split())
c=[[0 for i in range(b)]for j in range(a)]

for i in range(a):
  for j in range(b):
    if i%2==0 and j%2==0:
      c[i][j]='X'
    if i%2==0 and j%2==1:
      c[i][j]='.'
      
    if i%2==1 and j%2==1:
      c[i][j]='X'
    if i%2==1 and j%2==0:
      c[i][j]='.'
d=[]
for i in range(a):
    d.append(''.join(c[i]))  

dd=[]
dd1=[]
for i in range(a):
  for ii in range(aa):
    dd=[]
    for j in range(b):
      dd.append(d[i][j]*bb)
      dd1=''.join(dd)
    print(dd1)