a,b=map(int,input().split())
cnt=1
cnt1=0

while 1:
    if str(b) in str(cnt):
      cnt=cnt+1
      continue
    else:
      cnt=cnt+1
      cnt1=cnt1+1
    if cnt1 == a:
      break
print(cnt-1)