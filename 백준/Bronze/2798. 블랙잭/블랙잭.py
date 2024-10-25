a, b = map(int, input().split())
c = list(map(int, input().split()))
result = 0

# 세 개의 서로 다른 인덱스를 선택하여 합을 계산합니다.
for i in range(a):
    for j in range(i + 1, a):  # j는 i 다음 인덱스부터 시작
        for k in range(j + 1, a):  # k는 j 다음 인덱스부터 시작
            sum2 = c[i] + c[j] + c[k]
            if sum2 <= b:
                result = max(result, sum2)  # 현재 최대값 갱신

print(result)