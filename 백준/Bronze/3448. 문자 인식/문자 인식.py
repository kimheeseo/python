import sys

N = int(sys.stdin.readline())

for _ in range(N):
    R, A = 0, 0
    
    while True:
        line = sys.stdin.readline().rstrip()

        if not line:  # 빈 줄이 들어오면 종료
            break
        
        for char in line:
            if char == '#':
                A += 1
            else:
                A += 1
                R += 1
    
    ratio = round(R / A * 100, 1)

    # 소수점 아래가 0이면 정수로 출력
    if str(ratio).split('.')[-1] == '0':
        ratio = int(ratio)

    print(f'Efficiency ratio is {ratio}%.')