a=int(input())
cnt=0

b=list(map(int,input().split()))

for i in range(a):
    if b[i] ==1:
        cnt=cnt+1
    else:
        for j in range(2,int(b[i]**0.5)+1):
            if b[i]%j==0:
                cnt=cnt+1
                break
print(len(b)-cnt)