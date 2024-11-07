import sys
input=sys.stdin.readline

a=int(input())
b=list(map(int,input().split()))
total=sum(b)
d=0
minmin=float('inf')

for i in range(0,a-1):
  d=d+b[i] #left 값
  right=total-d #right 값

  cha=abs(right-d)
  minmin=min(minmin, cha)

print(minmin)