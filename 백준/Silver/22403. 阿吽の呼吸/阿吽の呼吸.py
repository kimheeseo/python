# 해당 문제는 마에다(A)와 고토(B)가 순서대로 말을 한다는 것이다.
# 예를 들어, AABB, ABAB는 규칙적이지만, ABBA와 같이 둘이 말한 횟수는 같지만,
# 규칙적이지 않은 것이니, deque으로 넣었다가 뺏다가 하면 된다.

from collections import deque

a = int(input())
b = deque()
error = 0

for _ in range(a):
    c = input()
    if c == 'A':
        b.append(c)
    else:
        if not b:
            error = 1
            break
        b.popleft()

if error == 1 or b:
    print("NO")
else:
    print("YES")