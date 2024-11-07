a=int(input())
b=list(map(int,input().split()))
sum1=0
sum2=0

for i in range(a):
  sum1=sum1+b[i]
for i in range(a):
  sum2=sum2+b[i]**2
print((sum1**2-sum2)//2)  