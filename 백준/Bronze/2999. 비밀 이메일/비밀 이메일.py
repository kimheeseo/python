str = input()           # 문자열 str 입력
len = len(str)          # 입력받은 문자열 길이 len

x, y = 0, 0

# 행 R개와 열 C개를 구하는 이중 반복문 (R이 커야 됨)
for r in range(1, int(len/2)+1):
    for c in range(r, len+1):
        if r*c == len:
            x, y = r, c

# 문자열 해독하는 과정
for i in range(x):
    for j in range(y):
        print(str[i+j*x], end='')