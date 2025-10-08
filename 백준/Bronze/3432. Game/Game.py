import sys

def has_three(board, ch):
    # 4방향: →, ↓, ↘, ↙
    dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in range(5):
        for j in range(5):
            if board[i][j] != ch:
                continue
            for dx, dy in dirs:
                x2, y2 = i + dx * 2, j + dy * 2
                if 0 <= x2 < 5 and 0 <= y2 < 5:
                    ok = True
                    for k in range(3):
                        x, y = i + dx * k, j + dy * k
                        if board[x][y] != ch:
                            ok = False
                            break
                    if ok:
                        return True
    return False

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        board = tokens[idx:idx+5]
        idx += 5
        a_win = has_three(board, 'A')
        b_win = has_three(board, 'B')
        if a_win and not b_win:
            out.append("A wins")
        elif b_win and not a_win:
            out.append("B wins")
        else:
            out.append("draw")
    print("\n".join(out))

if __name__ == "__main__":
    main()
