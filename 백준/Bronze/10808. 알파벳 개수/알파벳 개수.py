st = input()
st_cnt = [0] * 26

for s in st:
    n = ord(s) - ord('a')
    st_cnt[n] += 1

print(*st_cnt)