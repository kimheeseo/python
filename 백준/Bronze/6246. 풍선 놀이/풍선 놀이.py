import sys
input=sys.stdin.readline

a,b=map(int,input().split())
#a: 슬롯 수, b: 풍선들을 꽂는 횟수
d=['.']*int(a)
dd=['R','B','D']
cnt=0

for jj in range(b):
  q,w=map(int, input().split())
  for i in range(q-1,a,w):
    if d[i] not in dd:
      d[i]=dd[jj % len(dd)]
      cnt=cnt+1

print(a-cnt)