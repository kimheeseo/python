# a: 바구니 갯수, b: 입력 횟수
a, b = map(int, input().split())
basket = [0 for _ in range(a)]  # 바구니 초기화

for _ in range(b):  # 입력의 개수만큼 반복
    q, w, e = map(int, input().split())
    for j in range(q - 1, w):  # q부터 w까지의 바구니에 공 넣기 (0-indexed)
        basket[j] = e

# 결과 출력
print(" ".join(map(str, basket)))