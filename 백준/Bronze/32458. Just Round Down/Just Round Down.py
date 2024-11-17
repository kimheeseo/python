x = input().strip()  # 사용자로부터 입력을 받습니다.

# 입력된 문자열을 부동 소수점 숫자로 변환합니다.
float_number = float(x)

# 내림(floor) 함수 사용하여 정수로 변환합니다.
floor_value = int(float_number)  # 정수형으로 변환하면 자동으로 내림 처리됩니다.

# 결과 출력
print(floor_value)