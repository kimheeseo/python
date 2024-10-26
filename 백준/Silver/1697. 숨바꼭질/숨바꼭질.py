from collections import deque

def bfs(start, target):
    queue = deque([start])
    visited = [False] * 100001
    visited[start] = True
    distance = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == target:
                return distance
            
            # 가능한 다음 위치들
            next_positions = [current - 1, current + 1, current * 2]
            for next_pos in next_positions:
                if 0 <= next_pos <= 100000 and not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)
        
        distance += 1

start, target = map(int, input().split())
print(bfs(start, target))