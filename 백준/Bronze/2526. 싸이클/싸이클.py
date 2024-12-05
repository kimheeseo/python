a, b = map(int, input().split())
a1 = a
visited = {}  # 나머지를 기록할 딕셔너리

for i in range(1, b + 1):  # 최대 b번 반복
    a1 = (a1 * a) % b
    if a1 in visited:  # 이미 나온 값이라면 싸이클 시작
        print(i - visited[a1])  # 현재 인덱스 - 처음 나온 인덱스 = 싸이클 길이
        break
    visited[a1] = i  # 나머지와 해당 인덱스를 기록
