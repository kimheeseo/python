n = int(input())
parent = [int(input()) for _ in range(n)]
high = [0 for i in range(n)]

for i in range(n):
    if parent[i]==-1:
        continue
    high[i]=high[parent[i]-1]+1

for i in range(n):
    print(high[i])
# 출처: https://jh-0323.tistory.com/entry/%EB%B0%B1%EC%A4%80-13237%EB%B2%88-Binary-tree-python