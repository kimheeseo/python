def main():
    n = int(input())  # 입력받은 숫자를 정수로 변환
    
    for _ in range(n):
        arr = input().strip()  # 문자열 입력받음
        arr = arr.lower()  # 문자열을 소문자로 변환
        print(arr)  # 변환된 문자열 출력

if __name__ == "__main__":
    main()
