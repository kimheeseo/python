import sys
input=sys.stdin.readline
# 입력
P, K = map(int, input().split())

# K까지 나눠지는 수가 있는지 확인
for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")
    
# 소수의 곱으로 pq를 구하는 것이니까, p를 알아야 q를 알 수 있으니까.
# 이를 통해, 암호키로 사용한다.