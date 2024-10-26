a = int(input())
cnt = 0

# 5, 25, 125 등, 5의 제곱수의 배수를 고려
while a >= 5:
    a //= 5
    cnt += a

print(cnt)