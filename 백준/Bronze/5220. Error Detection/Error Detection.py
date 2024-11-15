for _ in range(int(input())):
    n, t = map(int, input().split())
    b = bin(n)[2:].count('1')
# b의 값은 n이라는 십진수의 값을 binary값으로 바꾼다음에 1의 갯수를 계산합니다.
# 만약 binary값과 2로 나눴을때의 나머지가 t와 같으면 유효(valid)
    print("Valid" if int(b)%2 == t else "Corrupt")