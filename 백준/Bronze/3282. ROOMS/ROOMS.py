N, G = map(int, input().split())
arr = [0] * 100
idx = 0
chk = False

for _ in range(G):
    M = int(input())
    while M:
        if chk:
            if arr[idx] == 2:
                idx += 1
            else:
                arr[idx] += 1
                idx += 1
                M -= 1
        else:
            if M == 1:
                arr[idx] = 1
                idx += 1
                M -= 1
            else:
                arr[idx] = 2
                idx += 1
                M -= 2

            if idx == N:
                chk = True
                idx = 0

for i in range(N):
    print(arr[i])