import sys
input=sys.stdin.readline
from collections import deque

a=int(input())
b=deque([i for i in range(1,a+1)])

while len(b)>1:
    b.popleft()
    q=b.popleft()
    b.append(q)  
    
a=b.popleft()
print(a)