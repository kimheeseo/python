import sys
input=sys.stdin.readline

a=int(input())
b=[]

for i in range(a):
  c=int(input())
  b.append(c)
print(sum(b)-(a-1))