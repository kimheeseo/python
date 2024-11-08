from collections import deque
a = int(input())
b = deque([i for i in range(1, a + 1)])
c = []

while len(b) > 1:  # b에 요소가 하나 이상 남을 때까지 반복
    w = b.popleft()
    q = b.popleft()
    b.append(q)
    c.append(w)

# b에 하나만 남았다면 그 값을 처리
if b:
    c.append(b.popleft())

for i in range(a):
    print(c[i], end=" ")