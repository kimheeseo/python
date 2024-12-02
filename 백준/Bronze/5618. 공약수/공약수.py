from math import gcd, sqrt
import sys
input=sys.stdin.readline
n = int(input())
lst = []

if n == 2:
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)


if n == 3:
    a, b, c = map(int, input().split())
    gcd_ = gcd(gcd(a, b), c)

for i in range(1, int(sqrt(gcd_)) + 1):
    if gcd_ % i == 0: # 22가 gcd일 때 1*22이면 1,22를 동시에 append하기 위해서.
        lst.append(i)
        if i**2 != gcd_:
            lst.append(gcd_ // i)
# 공약수 구할 때 계산 효율을 위해 int(sqrt(gcd_))+1 = int(gcd**0.5)+1 사용
lst.sort()

for num in lst:
    print(num)