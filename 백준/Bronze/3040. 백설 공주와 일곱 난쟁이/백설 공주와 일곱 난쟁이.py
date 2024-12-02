dwarfs = [int(input()) for _ in range(9)]

sum_dwarfs = sum(dwarfs)
# print(sum_dwarfs)


for i in range(9):
    for j in range(i+1,9):
        if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
            ### 배열에서 삭제가 어려울 땐 그냥 바로 정답 출력해버리기
            for k in range(9):
                if k not in [i,j]:
                    print(dwarfs[k])