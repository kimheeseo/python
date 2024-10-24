a,b=map(int, input().split())
c=list(map(int,input().split()))

for d in range(a):
  if c[d]<b:
    print(c[d], end =" ")