# 컴퓨터의 수와 연결 정보 입력 받기
n = int(input())  # 컴퓨터의 수
m = int(input())  # 연결의 수

# 인접 리스트로 그래프를 표현
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS를 이용해 감염된 컴퓨터 탐색
def dfs(v, visited):
    visited[v] = True
    count = 1  # 현재 노드가 감염된 컴퓨터로 카운트
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited)
    return count

# 1번 컴퓨터부터 시작해서 감염된 컴퓨터 수를 계산
visited = [False] * (n + 1)
infected_computers = dfs(1, visited) - 1  # 1번 컴퓨터는 제외하므로 -1

print(infected_computers)