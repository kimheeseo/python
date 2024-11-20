def main():
    K, N = map(int, input().split())
    # ranking 배열 초기화
    ranking = [[0] * (N + 1) for _ in range(K)]

    # K개의 순위표 입력 받기
    for i in range(K):
        positions = list(map(int, input().split()))
        for j in range(N):
            r = positions[j]
            ranking[i][r] = j

    ans = 0
    # i와 j를 비교
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            ok = True
            # K개의 순위표에서 i와 j 비교
            for k in range(K):
                if ranking[k][i] > ranking[k][j]:
                    ok = False
                    break
            if ok:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()