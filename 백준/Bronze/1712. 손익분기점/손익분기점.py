a,b,c=map(int,input().split())
cnt=0

if c-b <=0:
  print(-1)
else:
  cnt=a//(c-b)+1
  print(cnt) 