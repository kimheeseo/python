import sys
input=sys.stdin.readline

i=int(input())

for jj in range(i):
  a,b,c=map(int, input().split())
  qq=c//a
  ww=c%a
  if ww != 0:
    qq=qq+1
  else:
    ww=a
  print(ww*100+qq) 