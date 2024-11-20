a=int(input())
cnt=0

for i in range(a):
  b,c=map(str,input().split())
  h,m=b.split(':')
  time=int(h)*60+int(m)\

  for qwe in range(int(c)):
    if 420<= int(time) <1140:
      time=int(time)+1
      cnt=cnt+10
    else:
      time=int(time)+1
      cnt=cnt+5

print(cnt)