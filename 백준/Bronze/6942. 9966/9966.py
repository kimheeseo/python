def is_rotatable(number):
    # 180도 회전 가능한 숫자의 매핑
    mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    num_str = str(number)
    
    rotated = []
    for digit in reversed(num_str):  # 숫자를 뒤집어서 확인
        if digit not in mapping:  # 매핑되지 않는 숫자가 있으면 불가능
            return False
        rotated.append(mapping[digit])
    
    # 뒤집힌 숫자가 원래 숫자와 동일하면 True
    return ''.join(rotated) == num_str

def count_rotatable_numbers(m, n):
    count = 0
    for number in range(m, n + 1):
        if is_rotatable(number):
            count += 1
    return count

# 입력 처리
if __name__ == "__main__":
    m = int(input())
    n = int(input())
    result = count_rotatable_numbers(m, n)
    print(result)
