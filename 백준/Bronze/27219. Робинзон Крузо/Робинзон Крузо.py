n = int(input())

# 'V'를 n을 5로 나눈 몫만큼 출력
for i in range(n // 5):
    print("V", end="")

# 'I'를 n을 5로 나눈 나머지 만큼 출력
for i in range(n % 5):
    print("I", end="")