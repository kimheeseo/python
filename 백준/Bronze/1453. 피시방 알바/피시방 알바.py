a = int(input())
c = list(map(int, input().split()))

# 자리 번호의 최댓값을 기준으로 배열 크기 설정
max_seat = max(c)
b = [0] * max_seat
cnt = 0

for i in c:
    if b[i - 1] == 0:
        b[i - 1] = 1
    else:
        cnt += 1

print(cnt)