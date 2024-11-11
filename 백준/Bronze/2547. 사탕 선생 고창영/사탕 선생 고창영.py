import sys
input=sys.stdin.readline

a=int(input())

for i in range(a):
    cnt=0
    _=input()
    b=int(input())
    for j in range(b):
        c=int(input())
        cnt=cnt+c  
    if cnt%b ==0:
        print('YES')
    else:
        print('NO')