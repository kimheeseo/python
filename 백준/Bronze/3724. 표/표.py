import sys
input=sys.stdin.readline

za=int(input())
for qwe in range(za):
  a,b=map(int,input().split())
  ab=[0]*(a*b)

  for i in range(b):
    bb=list((map(int,input().split())))
    for j in range(a):
      ab[i*a+j]=bb[j]

  q=[1 for i in range(a)]
  for j in range(a):
    for i in range(b):
      q[j]=ab[i*a+j]*q[j]

  max_value=max(q)
  cnt=0
  for i in range(a):
    if q[i]==max_value:
      cnt=i
  print(cnt+1)