import sys
import math
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

# -------- Morton (Z-order) key: interleave 20-bit x, y --------
# x,y <= 814000 < 2^20, 그대로 20비트로 인터리브 가능
def _part1by1(n: int) -> int:
    # spread 20-bit integer so that there is one zero bit between each original bit
    n &= (1 << 20) - 1
    n = (n | (n << 16)) & 0x0000FFFF0000FFFF
    n = (n | (n << 8))  & 0x00FF00FF00FF00FF
    n = (n | (n << 4))  & 0x0F0F0F0F0F0F0F0F
    n = (n | (n << 2))  & 0x3333333333333333
    n = (n | (n << 1))  & 0x5555555555555555
    return n

def morton_key(x: int, y: int) -> int:
    return (_part1by1(x) << 1) | _part1by1(y)

# -------- distance helpers --------
def dist(a, b):
    # a,b: (x,y)
    return math.hypot(a[0]-b[0], a[1]-b[1])

def nn_tour(points):
    """
    최근접 이웃으로 초기 경로 생성.
    points: list of (x,y,idx)
    return: order (list of indices)
    """
    m = len(points)
    if m == 1:
        return [points[0][2]]
    # start: 가운데쯤 점 하나
    start = m // 2
    used = [False] * m
    order = [start]
    used[start] = True

    # 전처리: 좌표만
    coords = [(px, py) for (px, py, _) in points]

    cur = start
    for _ in range(m-1):
        best = -1
        best_d2 = None
        cx, cy = coords[cur]
        # sqrt 생략하고 제곱거리 비교
        for j in range(m):
            if not used[j]:
                dx = coords[j][0] - cx
                dy = coords[j][1] - cy
                d2 = dx*dx + dy*dy
                if best == -1 or d2 < best_d2:
                    best = j
                    best_d2 = d2
        used[best] = True
        order.append(best)
        cur = best

    return [points[i][2] for i in order]

def tour_length(order_idx, points_by_id):
    # order_idx: list of city-id (1-based)
    # points_by_id: dict id -> (x,y)
    s = 0.0
    m = len(order_idx)
    for i in range(m):
        a = points_by_id[order_idx[i]]
        b = points_by_id[order_idx[(i+1) % m]]
        s += math.hypot(a[0]-b[0], a[1]-b[1])
    return s

def two_opt(order_idx, points_by_id, max_pass=2):
    """
    간단한 2-opt: max_pass 번의 풀 스윕. m≈60 기준 충분히 빠름.
    """
    m = len(order_idx)
    if m <= 3:
        return order_idx

    coords = [points_by_id[i] for i in order_idx]

    def seg_len(a, b):
        ax, ay = a; bx, by = b
        return math.hypot(ax-bx, ay-by)

    improved = True
    pass_cnt = 0
    while improved and pass_cnt < max_pass:
        improved = False
        pass_cnt += 1
        # 표준 2-opt (i, i+1) vs (j, j+1), with wrap-around 제외
        for i in range(m - 1):
            a, b = coords[i], coords[(i+1) % m]
            for j in range(i + 2, m - (0 if i > 0 else 1)):
                c, d = coords[j], coords[(j+1) % m]
                # 기존: ab + cd , 교체: ac + bd
                if seg_len(a, b) + seg_len(c, d) > seg_len(a, c) + seg_len(b, d) + 1e-9:
                    # reverse (i+1 .. j)
                    order_idx[i+1:j+1] = reversed(order_idx[i+1:j+1])
                    coords[i+1:j+1] = reversed(coords[i+1:j+1])
                    improved = True
        # 끝

    return order_idx

def main():
    N_K = input().split()
    while len(N_K) < 2:
        N_K += input().split()
    N, K = map(int, N_K)
    pts = []
    for i in range(1, N+1):
        x, y = map(int, input().split())
        pts.append((x, y, i))

    # 1) Morton key로 정렬
    pts.sort(key=lambda t: morton_key(t[0], t[1]))

    # 2) K개 그룹으로 연속 분할 (앞쪽에 +1 분배)
    base = N // K
    rem = N % K
    sizes = [base + 1 if i < rem else base for i in range(K)]

    # id -> (x,y) 빠른 접근용
    points_by_id = {idx: (x, y) for (x, y, idx) in pts}

    out_lines = []
    pos = 0
    for g in range(K):
        sz = sizes[g]
        group = pts[pos:pos+sz]
        pos += sz

        # 3) 각 그룹 경로: NN + 2-opt
        order = nn_tour(group)
        # 작은 그룹은 opt 패스 1, 중간 이상은 2
        max_pass = 1 if sz <= 25 else 2
        order = two_opt(order, points_by_id, max_pass=max_pass)

        out_lines.append(str(sz) + " " + " ".join(map(str, order)))

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
