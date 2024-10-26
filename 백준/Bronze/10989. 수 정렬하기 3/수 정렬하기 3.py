import sys
input = sys.stdin.readline

a = int(input())
count = [0] * 10001  # 숫자의 범위가 1부터 10,000이므로 크기를 10,001로 설정

# 입력받은 숫자의 개수를 계수 배열에 저장
for _ in range(a):
    c = int(input())
    count[c] += 1

# 결과 출력
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)