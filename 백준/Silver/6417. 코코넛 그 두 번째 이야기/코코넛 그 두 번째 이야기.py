import sys
import math

def ok(N: int, K: int) -> bool:
    t = N
    for _ in range(K):
        if t % K != 1:
            return False
        t = (t - 1) * (K - 1) // K
    return t % K == 0

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        N = int(line)
        if N == -1:
            break

        maxK = 0
        # 많은 풀이가 K를 2..sqrt(N)까지만 검사합니다.
        LIM = int(math.isqrt(N)) + 1
        for K in range(2, LIM + 1):
            if ok(N, K):
                maxK = K

        if maxK >= 2:
            out.append(f"{N} coconuts, {maxK} people and 1 monkey")
        else:
            out.append(f"{N} coconuts, no solution")

    print("\n".join(out))

if __name__ == "__main__":
    main()
