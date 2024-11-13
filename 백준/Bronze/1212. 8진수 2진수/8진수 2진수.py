import sys
input = sys.stdin.readline

# 8진수 각 자릿수를 2진수로 변환하기 위한 매핑
octal_to_binary = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': '011',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111'
}

# 입력 받은 8진수 문자열
octal_number = input().strip()

# 결과를 저장할 2진수 문자열
binary_number = ''.join(octal_to_binary[digit] for digit in octal_number)

# 결과 출력 (맨 앞의 불필요한 '0' 제거)
print(binary_number.lstrip('0') or '0')