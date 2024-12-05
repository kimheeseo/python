def main():
    # 입력 받기
    R, C = map(int, input().split())  # R: 행, C: 열
    s = [input().strip() for _ in range(R)]  # 각 행의 문자열 입력받기

    # 결과 저장을 위한 배열 초기화
    result = [0] * 5

    # 모든 칸을 탐색
    for i in range(R - 1):
        for j in range(C - 1):
            # 2x2 영역 확인
            temp = 0
            # 건물이 있으면 스킵
            if (
                s[i][j] == "#" or s[i][j + 1] == "#" or
                s[i + 1][j] == "#" or s[i + 1][j + 1] == "#"
            ):
                continue

            # X의 개수 세기
            if s[i][j] == "X":
                temp += 1
            if s[i + 1][j] == "X":
                temp += 1
            if s[i][j + 1] == "X":
                temp += 1
            if s[i + 1][j + 1] == "X":
                temp += 1

            # 결과 업데이트
            result[temp] += 1

    # 결과 출력
    for count in result:
        print(count)

if __name__ == "__main__":
    main()
