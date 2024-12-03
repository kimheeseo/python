candy = int(input())
cnt = 0
for a in range(1, candy-2 + 1): # taqui
    for b in range(1, candy-2 + 1): # yeonghun
        for c in range(1, candy-2 + 1): # namgyu
            if a+b+c != candy:
                continue
            if c < 2 + b: # 수정
                continue
            if a % 2 == 1:
                continue
            cnt+=1
print(cnt)