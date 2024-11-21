n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

a, b = 0, 0

# 행을 확인
for i in range(n):
    if "X" not in board[i]:
        a += 1

# 열을 확인
for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:
        b += 1

# a와 b 중 더 큰 값 출력
print(max(a, b))