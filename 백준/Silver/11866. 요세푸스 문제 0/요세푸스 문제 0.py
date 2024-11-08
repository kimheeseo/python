from collections import deque

a, b = map(int, input().split())
queue = deque([i for i in range(1, a + 1)])

result = []

while queue:
    queue.rotate(-(b - 1))  # b-1번 회전
    result.append(queue.popleft())  # b번째 사람을 제거하고 결과에 추가

# 출력 형식 맞추기
print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")