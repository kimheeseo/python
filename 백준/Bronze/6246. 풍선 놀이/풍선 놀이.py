a, b = map(int, input().split())  # a: 슬롯 수, b: 풍선들을 꽂는 횟수
d = ['.'] * a  # 슬롯 상태 초기화
dd = ['R', 'B', 'D']  # 풍선 색상 순서
cnt = 0  # 꽂힌 풍선 개수

for jj in range(b):
    q, w = map(int, input().split())  # q: 시작, w: 간격
    for i in range(q - 1, a, w):  # q-1부터 시작, w 간격으로 진행
        if d[i] == '.':  # 슬롯이 비어 있는 경우
            d[i] = dd[jj % len(dd)]  # 색상 순환
            cnt += 1  # 꽂은 풍선 개수 증가

# 결과 출력
print(a - cnt)  # 빈 슬롯 개수 출력