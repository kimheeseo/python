import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    x, y = map(int, data[0].split())
    
    # 2차원 배열 입력 받기
    c = []
    for i in range(1, x + 1):
        c.append(list(map(int, data[i].split())))

    max_sum = 0
    max_position = (0, 0)

    # 3x3 부분 행렬 합 계산
    for i in range(x - 2):
        for j in range(y - 2):
            current_sum = counting(c, i, j)
            if current_sum > max_sum:
                max_sum = current_sum
                max_position = (i + 1, j + 1)

    print(max_sum)
    print(max_position[0], max_position[1])

def counting(c, i, j):
    # 3x3 부분 행렬의 합 계산
    count = 0
    for q in range(i, i + 3):
        for w in range(j, j + 3):
            count += c[q][w]
    return count
if __name__ == "__main__":
    main()