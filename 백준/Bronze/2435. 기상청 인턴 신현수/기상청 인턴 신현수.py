a, b = map(int, input().split())
d = list(map(int, input().split()))

max_sum = -float('inf')  # 초기 최대 합을 매우 작은 값으로 설정

for i in range(a - b + 1):  # i의 범위를 조정하여 인덱스 초과 방지
    current_sum = 0
    for j in range(i, i + b):
        current_sum += d[j]
    if max_sum < current_sum:
        max_sum = current_sum

print(max_sum)