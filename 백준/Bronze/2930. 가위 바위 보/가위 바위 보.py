import sys
def main():
    r = int(sys.stdin.readline())  # 라운드 수
    sg = list(sys.stdin.readline().strip())  # 각 라운드별 상근이가 낸 모양
    n = int(sys.stdin.readline())  # 친구들 수

    # 각 라운드마다 가위(S), 바위(R), 보(P)를 낸 친구 수를 구하기
    times = [[0, 0, 0] for _ in range(r)]  # 여기에 저장
    for _ in range(n):  # 친구의 명수만큼 반복
        temp = list(sys.stdin.readline().strip())  # 이번 친구가 낸 모양들을 읽어오기
        for j in range(r):
            if temp[j] == 'S':  # 가위
                times[j][0] += 1
            elif temp[j] == 'R':  # 바위
                times[j][1] += 1
            else:  # 보
                times[j][2] += 1

    # 상근이의 점수 구하기
    score1 = 0
    for i in range(r):
        mine = sg[i]  # 상근이가 이번에 낸 모양
        if mine == 'S':  # 상근이가 가위를 낸 라운드
            score1 += 2 * times[i][2] + times[i][0]
        elif mine == 'R':  # 상근이가 바위를 낸 라운드
            score1 += 2 * times[i][0] + times[i][1]
        else:  # 상근이가 보를 낸 라운드
            score1 += 2 * times[i][1] + times[i][2]

    # 상근이가 얻을 수 있는 최대 점수 구하기
    score2 = 0
    for i in range(r):
        # 이번 라운드에서 상근이가 각각 가위(srp[0]), 바위(srp[1]), 보(srp[2])를 냈을 때 얻는 점수
        srp = [
            2 * times[i][2] + times[i][0],
            2 * times[i][0] + times[i][1],
            2 * times[i][1] + times[i][2]
        ]
        # 셋 중 최댓값 취하기
        score2 += max(srp)

    # 정답 출력하기
    print(score1)
    print(score2)

if __name__ == "__main__":
    main()