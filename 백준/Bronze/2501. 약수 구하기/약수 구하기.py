a,q=map(int, (input().split()))
b=[]

for i in range(1,a+1):
  if a%i==0:
    b.append(i)

if q>len(b):
  print(0)
else:
  print(b[q-1])
