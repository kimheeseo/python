a=int(input())

for i in range(a):
    q,w,e=map(int,input().split())
    print(q*(e-1)+w)