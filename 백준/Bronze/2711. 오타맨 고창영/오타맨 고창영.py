a=int(input())
from collections import deque
for i in range(a):
  b,c=input().split()
  c=list(c)
  d=deque(c)
  d.rotate(-(int(b)-1))
  d.popleft()
  d.rotate(int(b)-1)
  dd=[]
  for i in range(len(d)):
    dd.append(d.popleft())
  
  dd=''.join(dd)
  print(dd)