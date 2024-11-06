ii=int(input())
cnt=0

for i in range(ii):
  cnt=0
  a,b,c=map(int,input().split())
  for q in range(1, a+1):
    for w in range(1,b+1):
      for e in range(1,c+1):
        if q%w == w%e == e%q:
          cnt=cnt+1
  print(cnt)
