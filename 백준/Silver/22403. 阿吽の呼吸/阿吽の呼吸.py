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