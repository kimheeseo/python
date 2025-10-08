import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1+n]

    # prefix: 앞에서 i개 중 '2'의 개수
    pref2 = [0] * (n + 1)
    for i in range(1, n + 1):
        pref2[i] = pref2[i - 1] + (1 if a[i - 1] == 2 else 0)

    # suffix: i..n-1 중 '1'의 개수
    suf1 = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf1[i] = suf1[i + 1] + (1 if a[i] == 1 else 0)

    ans = min(pref2[i] + suf1[i] for i in range(n + 1))
    print(ans)

if __name__ == "__main__":
    solve()
