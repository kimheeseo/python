import sys
input=sys.stdin.readline

c=int(input()) # 몇 번 반복할지?
d=list(map(int,input().split()))

cc=int(input())

for ii in range(cc):
    cnt=0
    i, j = map(int, input().split())
    cnt=cnt+sum(d[i:j+1])
    print(cnt)