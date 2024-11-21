def check(num):
    # 숫자를 문자열로 변환하여 '7'이 포함되어 있는지 확인
    return '7' in str(num)

def main():
    # 입력 받기
    num = int(input().strip())

    if check(num):  # 7이 포함된다면
        if num % 7 != 0:  # 7로 나뉘지 않는다면
            print(2)
        else:  # 나뉜다면
            print(3)
    else:  # 7이 포함되지 않는다면
        if num % 7 != 0:
            print(0)
        else:
            print(1)

if __name__ == "__main__":
    main()