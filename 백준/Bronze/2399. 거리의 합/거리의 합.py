import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))

# 배열을 정렬
b.sort()

# 누적합 계산
prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + b[i - 1]

cnt = 0

# 각 요소가 얼마나 기여하는지 계산
for i in range(a):
    cnt += (b[i] * i - prefix_sum[i])  # i번째 수가 작은 쪽에 얼마나 기여하는지
    cnt += ((prefix_sum[a] - prefix_sum[i + 1]) - b[i] * (a - i - 1))  # i번째 수가 큰 쪽에 얼마나 기여하는지

print(cnt)