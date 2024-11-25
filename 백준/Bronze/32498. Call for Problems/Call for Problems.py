import sys

# 입력을 받기 위해 sys.stdin을 사용합니다.
input = sys.stdin.read
data = input().split()

# 문제의 개수
n = int(data[0])
count = 0

# 문제의 개수만큼 반복문
for i in range(1, n + 1):
    rank = int(data[i])
    
    # 홀수인지 판별
    if rank % 2 == 1:
        count += 1

# 결과 출력
print(count)