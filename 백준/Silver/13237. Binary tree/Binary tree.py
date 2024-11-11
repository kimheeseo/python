n = int(input())
parent = [int(input()) for _ in range(n)]
high = [0 for i in range(n)]

for i in range(n):
    if parent[i]==-1:
        continue
    high[i]=high[parent[i]-1]+1

for i in range(n):
    print(high[i])