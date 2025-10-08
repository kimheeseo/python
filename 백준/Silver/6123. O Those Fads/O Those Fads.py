import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n = next(it); L = next(it); K = next(it)

    r = [next(it) for _ in range(n)]
    r.sort()

    cnt = 0
    for x in r:
        if x <= L:
            cnt += 1
            L += K
        else:
            break

    print(cnt)

if __name__ == "__main__":
    main()
