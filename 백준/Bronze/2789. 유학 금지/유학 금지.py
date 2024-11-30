# 입력받기
s = input()

# 제외할 문자들
exclude_chars = {'C', 'A', 'M', 'B', 'E', 'R', 'I', 'D', 'G'}

# 결과 문자열 생성 및 출력
result = ''.join(char for char in s if char not in exclude_chars)
print(result)