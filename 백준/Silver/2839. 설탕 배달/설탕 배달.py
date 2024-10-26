a = int(input())
result = -1  # 초기값을 -1로 설정하여 정확히 나눌 수 없는 경우 대비

# 5kg 봉지의 개수를 최대한 많이 사용하며 나머지를 3kg 봉지로 나눌 수 있는지 확인
for i in range(a // 5, -1, -1):  # 5kg 봉지 최대 개수부터 시작하여 0까지 감소
    remaining = a - (5 * i)  # 5kg 봉지 사용 후 남은 설탕 무게
    if remaining % 3 == 0:  # 나머지가 3으로 나눠지면
        result = i + (remaining // 3)  # 5kg 봉지 수 + 3kg 봉지 수
        break

print(result)