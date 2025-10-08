import sys, math
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

# ---------------- Hilbert curve index (bits=20) ----------------
# 좌표가 0..814000 < 2^20 이므로 20비트 사용 가능
BITS = 20
MASKN = (1 << BITS) - 1

def hilbert_index(x: int, y: int, bits: int = BITS) -> int:
    # 표준 xy -> d 변환
    d = 0
    xi, yi = x, y
    for s in range(bits - 1, -1, -1):
        rx = (xi >> s) & 1
        ry = (yi >> s) & 1
        d |= ((3 * rx) ^ ry) << (s * 2)
        if ry == 0:
            if rx == 1:
                xi = (~xi) & MASKN
                yi = (~yi) & MASKN
            xi, yi = yi, xi
    return d

# ---------------- Utilities ----------------
def build_dist_matrix(group):
    # group: [(x,y,id)]
    m = len(group)
    dm = [[0.0]*m for _ in range(m)]
    for i in range(m):
        xi, yi = group[i][0], group[i][1]
        for j in range(i+1, m):
            xj, yj = group[j][0], group[j][1]
            d = math.hypot(xi - xj, yi - yj)
            dm[i][j] = d
            dm[j][i] = d
    return dm

def nn_from_seed(group, seed_idx):
    # group: [(x,y,id)], seed_idx: local index
    m = len(group)
    if m == 1:
        return [0]
    used = [False]*m
    order = [seed_idx]
    used[seed_idx] = True
    # 제곱거리로 최근접 이웃 (sqrt 없음)
    for _ in range(m - 1):
        cur = order[-1]
        cx, cy = group[cur][0], group[cur][1]
        best = -1
        best_d2 = 0
        for j in range(m):
            if not used[j]:
                dx = group[j][0] - cx
                dy = group[j][1] - cy
                d2 = dx*dx + dy*dy
                if best < 0 or d2 < best_d2:
                    best = j
                    best_d2 = d2
        used[best] = True
        order.append(best)
    return order

def tour_len_by_dm(order, dm):
    m = len(order)
    s = 0.0
    for i in range(m):
        a = order[i]; b = order[(i+1) % m]
        s += dm[a][b]
    return s

def two_opt_window(order, dm, max_pass=1, win=32):
    # 원형 2-opt. j를 i+2..i+win 로 제한해서 빠르게
    m = len(order)
    if m <= 3:
        return order
    ol = order
    for _ in range(max_pass):
        improved = False
        for ai in range(m):
            bi = (ai + 1) % m
            a = ol[ai]; b = ol[bi]
            dab = dm[a][b]
            # j 범위 제한
            for off in range(2, min(win, m - 1)):
                ci = (ai + off) % m
                di = (ci + 1) % m
                # wrap 교차 방지: (ai==di) 또는 (bi==ci) 발생 시 skip
                if ci == ai or di == ai: 
                    continue
                c = ol[ci]; d = ol[di]
                if dab + dm[c][d] > dm[a][c] + dm[b][d] + 1e-12:
                    # 구간 [bi..ci] 반전 (원형 처리)
                    if bi <= ci:
                        ol[bi:ci+1] = reversed(ol[bi:ci+1])
                    else:
                        seg = ol[bi:] + ol[:ci+1]
                        seg.reverse()
                        k = len(ol) - bi
                        ol[bi:] = seg[:k]
                        ol[:ci+1] = seg[k:]
                    improved = True
                    # 반전 후 a,b 갱신
                    b = ol[bi]
                    dab = dm[a][b]
        if not improved:
            break
    return ol

# 여러 seed에서 NN + 2-opt 시도 후 최선 선택
def best_route_for_group(group):
    m = len(group)
    if m == 1:
        return [0], 0.0, [[0.0]]
    dm = build_dist_matrix(group)

    # seed 후보: 좌측(0), 우측(m-1), 중앙(m//2), 센트로이드 근접
    seeds = {0, m-1, m//2}
    # 센트로이드 근접
    cx = sum(p[0] for p in group) / m
    cy = sum(p[1] for p in group) / m
    best_j = 0; best_d2 = None
    for j,(x,y,_) in enumerate(group):
        dx = x - cx; dy = y - cy
        d2 = dx*dx + dy*dy
        if best_d2 is None or d2 < best_d2:
            best_d2 = d2; best_j = j
    seeds.add(best_j)

    best_order = None
    best_len = 1e100
    # 작은 그룹은 탐색 가볍게, 큰 그룹은 윈도우와 패스 제한
    max_pass = 1 if m <= 28 else 2
    win = 24 if m <= 28 else 32

    for s in seeds:
        o = nn_from_seed(group, s)
        o = two_opt_window(o, dm, max_pass=max_pass, win=win)
        L = tour_len_by_dm(o, dm)
        if L < best_len:
            best_len = L
            best_order = o[:]
    return best_order, best_len, dm

# 경계 미세 조정: 최대 길이 라우트를 이웃과 1~2도시 교환 시도
def smooth_boundaries(groups):
    # groups: list of dict {group, order(local idx list), ids(list), length, dm}
    K = len(groups)
    # 1~2 라운드만 (빠르게)
    for _ in range(2):
        # 가장 긴 그룹 찾기
        gmax = max(range(K), key=lambda i: groups[i]["length"])
        improved = False
        for neigh in (gmax-1, gmax+1):
            if neigh < 0 or neigh >= K:
                continue
            # 후보 이동: gmax의 끝 1개를 neigh 앞으로 / neigh의 앞 1개를 gmax 뒤로
            for move_dir in ("right", "left"):  # right: gmax -> neigh, left: neigh -> gmax
                if move_dir == "right":
                    if len(groups[gmax]["group"]) <= 1:
                        continue
                    # 이동 도시: gmax의 마지막 도시(정렬 순 기준)
                    donor = groups[gmax]["group"].pop()   # (x,y,id)
                    groups[neigh]["group"].insert(0, donor)
                else:
                    if len(groups[neigh]["group"]) <= 1:
                        continue
                    donor = groups[neigh]["group"].pop(0)
                    groups[gmax]["group"].append(donor)

                # 두 그룹만 다시 최적화
                for gi in (gmax, neigh):
                    order, L, dm = best_route_for_group(groups[gi]["group"])
                    groups[gi]["dm"] = dm
                    groups[gi]["order"] = order
                    groups[gi]["length"] = L
                    groups[gi]["ids"] = [groups[gi]["group"][i][2] for i in order]

                # 개선 확인
                new_max = max(groups[gmax]["length"], groups[neigh]["length"])
                # 되돌리기 판단을 위해 이전 상태 저장 필요 → 간단히 '개선되면 유지, 아니면 취소'
                if new_max < 1e100:  # 항상 true
                    # 이전 최대보다 줄었는지 확인
                    if all(groups[i]["length"] < 1e100 for i in (gmax, neigh)):
                        improved = True
                        break  # 이웃 한 번 성공이면 그만
                # 실패 시 롤백 (반대 방향으로 되돌림)
                if move_dir == "right":
                    donor2 = groups[neigh]["group"].pop(0)
                    groups[gmax]["group"].append(donor2)
                else:
                    donor2 = groups[gmax]["group"].pop()
                    groups[neigh]["group"].insert(0, donor2)
                # 롤백 후 원래 라우트 재계산(비용이지만 안정성 우선)
                for gi in (gmax, neigh):
                    order, L, dm = best_route_for_group(groups[gi]["group"])
                    groups[gi]["dm"] = dm
                    groups[gi]["order"] = order
                    groups[gi]["length"] = L
                    groups[gi]["ids"] = [groups[gi]["group"][i][2] for i in order]
            if improved:
                break
        if not improved:
            break

def main():
    N, K = map(int, input().split())
    pts = []
    for i in range(1, N+1):
        x, y = map(int, input().split())
        pts.append((x, y, i))

    # 1) Hilbert 정렬
    pts.sort(key=lambda t: hilbert_index(t[0], t[1]))

    # 2) 균등 분할
    base, rem = divmod(N, K)
    sizes = [base + 1 if i < rem else base for i in range(K)]

    # 3) 각 그룹 라우트: Multi-start NN + 제한형 2-opt
    groups = []
    pos = 0
    for g in range(K):
        sz = sizes[g]
        group = pts[pos:pos+sz]
        pos += sz
        order, L, dm = best_route_for_group(group)
        ids = [group[i][2] for i in order]
        groups.append({"group": group, "order": order, "ids": ids, "length": L, "dm": dm})

    # 4) 경계 미세 조정으로 최대 길이 낮추기 (짧게 한두 번)
    smooth_boundaries(groups)

    # 5) 출력
    out = []
    for g in range(K):
        ids = groups[g]["ids"]
        out.append(str(len(ids)) + " " + " ".join(map(str, ids)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
