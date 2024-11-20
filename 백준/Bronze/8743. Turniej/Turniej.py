import sys
input=sys.stdin.readline

# 입력 데이터 받기
z = int(input())  # 테스트 케이스 수

# 각 테스트 케이스에 대해 결과 계산
results = []
for _ in range(z):
    n, k = map(int, input().split())
    # 우승자가 될 수 있는 최대 인원의 수 계산
    results.append(str(min(n, k - 1)))

# 결과 출력
print("\n".join(results))