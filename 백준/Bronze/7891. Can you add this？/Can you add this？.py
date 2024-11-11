# 테스트 케이스의 개수를 입력
t = int(input())

# t번의 테스트를 수행
for _ in range(t):
    # 정수 x와 y를 공백을 기준으로 분리하여 입력
    a, b = map(int, input().split())

    # 정수 x와 y의 합을 계산하여 출력
    print(a + b)