a=int(input())
b=list(input().split())
c=list(input().split())

sum=0

for i in range(0,a):
    if int(b[i]) <= int(c[i]):
        sum+=1
print(sum)