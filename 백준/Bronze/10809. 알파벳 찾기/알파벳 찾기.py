s=list(input())
a='abcdefghijklmnopqrstuvwxyz'

for j in a:
  if j in s:
    print(s.index(j), end=" ")
  else:
    print(-1, end=" ")