a=[]
c=[]
for i in range(10):
  a.append(int(input()))

for ii in range(len(a)):
  if a[ii]<42:
    c.append(a[ii])
  if a[ii]>=42:
    c.append(a[ii]%42)
d=list(set(c))
print(len(d))