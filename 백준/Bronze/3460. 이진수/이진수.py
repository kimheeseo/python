T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")
# bin을 통해 이진수로 만든 다음에, "1"의 위치를 찾아서 수행.