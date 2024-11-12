import sys
input=sys.stdin.readline

T = int(input())
score = list(map(int, input().split()))
cnt = 0     # 연속된 점수일 경우 더해준다.
answer = []
for i in score:
    if i == 1:
        answer.append(1 + cnt)
        cnt += 1
    elif i == 0:
        answer.append(0)
        cnt = 0

print(sum(answer))