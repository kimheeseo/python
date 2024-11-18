from collections import deque
a,b=map(int, input().split())
c=deque(map(int, input().split(',')))

for ii in range(b):
  i=0
  for j in range(len(c)-1):
    d=c[i+1]-c[i]
    c.popleft()
    c.append(d)
  c.popleft()    

for i in range(len(c)):
  if i == len(c)-1:
    print(c[i])
    break
  print(c[i], end=",")
