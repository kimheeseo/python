import sys
input = sys.stdin.readline

a = int(input())  # a는 입력받지만 실제로 사용되지 않음
b = list(map(int, input().split()))

total_sum = sum(b)
total_square_sum = sum(x * x for x in b)

# 전체 합의 제곱에서 각 b[i]^2를 빼면 우리가 원하는 결과
result = total_sum * total_sum - total_square_sum
print(result // 2%1000000007)