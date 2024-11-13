a=int(input())
b=list(map(int,input().split()))
c=int(input())
cnt=0

for i in range(a):
  if b[i] == 0:
    continue
  if b[i]//c ==0:
    cnt=cnt+1
  elif b[i]%c==0:
    cnt=cnt+b[i]//c
  else:
    cnt=cnt+b[i]//c+1
print(cnt*c)