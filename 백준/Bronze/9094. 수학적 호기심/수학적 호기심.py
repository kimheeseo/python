import sys
input=sys.stdin.readline
a=int(input())

for jj in range(a):
    cnt=0
    n,m=map(int,input().split())
    for i in range(1,n):
        for j in range(i+1, n):
            if (i**2+j**2+m)%(i*j) == 0:
                cnt=cnt+1
             
    print(cnt)