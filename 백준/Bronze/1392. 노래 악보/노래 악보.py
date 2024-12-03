import sys
input=sys.stdin.readline

N, Q = map(int, sys.stdin.readline().split())

musicList = [int(sys.stdin.readline()) for _ in range(N)]
findList = [int(sys.stdin.readline()) for _ in range(Q)]

result = []
i = 1
for item in musicList:
    for _ in range(item):
        result.append(i)
    i = i + 1

for item in findList:
    print(result[item])