import sys
input=sys.stdin.readline

for i in range(int(input())):
    n=int(input())
    a=0
    sum=0
    for j in range(1,n+1):
        for k in range(1, j+2): #T(k+1)을 나타내는 부분
            a=a+k #k* T(k+1)
        sum=sum+a*j
        a=0
    print(sum)