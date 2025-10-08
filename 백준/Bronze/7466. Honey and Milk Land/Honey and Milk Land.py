import sys
import math

def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n = next(it); e = next(it)

    W = 0
    if n > 1:
        for _ in range(n - 1):
            W += next(it)

    H = 0
    if e > 1:
        for _ in range(e - 1):
            H += next(it)

    s = W * W + H * H  # W^2 + H^2
    r = math.isqrt(s)  # floor(sqrt(s))
    ans = r if r * r == s else r + 1  # ceil(sqrt(s))
    print(ans)

if __name__ == "__main__":
    main()
