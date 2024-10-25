a=int(input()) #영수증에 적힌 총 금액
b=int(input()) #영수증에 적힌 구매한 물건의 종류의 수
sum=0

for c in range(b):
    d,e=map(int, input().split())
    sum=d*e+sum
    
if sum==a:
    print('Yes')
else:
    print('No')