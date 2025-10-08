import sys
from functools import cmp_to_key

def cmp(a, b):
    # a, b: (J, P, idx)
    Ja, Pa, ia = a
    Jb, Pb, ib = b
    # 내림차순: r_a > r_b 이면 a가 먼저
    lhs = Ja * Pb
    rhs = Jb * Pa
    if lhs != rhs:
        return -1 if lhs > rhs else 1
    # 비율 동률이면 가격 오름차순
    if Pa != Pb:
        return -1 if Pa < Pb else 1
    # 그래도 같으면 인덱스 오름차순
    return -1 if ia < ib else (1 if ia > ib else 0)

def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n = next(it)
    toys = []
    for i in range(1, n + 1):
        J = next(it); P = next(it)
        toys.append((J, P, i))

    toys.sort(key=cmp_to_key(cmp))
    pick = toys[:3]

    total_price = sum(p for _, p, _ in pick)
    print(total_price)
    for _, _, idx in pick:
        print(idx)

if __name__ == "__main__":
    main()
