import math

def maxdigit(p, q, r):
    # 세 수 p, q, r에서 가장 큰 자릿수를 찾음
    max_digit = 0
    for num in [p, q, r]:
        while num > 0:
            max_digit = max(max_digit, num % 10)
            num //= 10
    return max_digit

def todecimal(x, n):
    # n진법으로 표현된 수 x를 10진법으로 변환
    decimal = 0
    i = 0
    while x > 0:
        decimal += (x % 10) * (n ** i)
        x //= 10
        i += 1
    return decimal

def main():
    T = int(input())  # 테스트 케이스 개수 입력

    for _ in range(T):
        p, q, r = map(int, input().split())  # 세 수 p, q, r 입력
        solved = False

        # 가능한 진법을 탐색
        for n in range(maxdigit(p, q, r) + 1, 17):
            if todecimal(p, n) * todecimal(q, n) == todecimal(r, n):
                print(n)
                solved = True
                break

        if not solved:
            print(0)

if __name__ == "__main__":
    main()
