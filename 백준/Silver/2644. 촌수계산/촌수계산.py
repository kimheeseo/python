n = int(input())  # 전체 사람 수
aa, bb = map(int, input().split())  # 촌수를 계산할 두 사람
m = int(input())  # 관계 수
arr = [[0] * n for _ in range(n)]  # 인접 행렬
visit = [-1] * n  # 방문 여부와 촌수를 저장하는 리스트 (-1로 초기화)

# 관계를 인접 행렬에 저장
for _ in range(m):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = arr[y - 1][x - 1] = 1

def bfs(x):
    queue = [x]
    visit[x] = 0  # 시작 노드의 촌수를 0으로 초기화
    
    while queue:
        now = queue.pop(0)
        for i in range(n):
            if arr[now][i] == 1 and visit[i] == -1:  # 연결되어 있고 미방문인 경우
                visit[i] = visit[now] + 1  # 이전 촌수 + 1
                queue.append(i)

# aa에서 시작하여 촌수를 계산
bfs(aa - 1)

# 결과 출력: bb에 도달할 수 없으면 -1, 도달하면 촌수를 출력
print(visit[bb - 1] if visit[bb - 1] != -1 else -1)