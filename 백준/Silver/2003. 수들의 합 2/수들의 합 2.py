import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left = right = 0
cur = 0
cnt = 0

# 모든 원소가 양수일 때: 투 포인터 O(N)
while True:
    if cur >= M:
        if cur == M:
            cnt += 1
        cur -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        cur += nums[right]
        right += 1

print(cnt)
