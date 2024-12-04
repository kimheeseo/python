import sys
input=sys.stdin.readline

def is_safe(rooks):
    rows = set()
    cols = set()
    for col, row in rooks:
        if row in rows or col in cols:
            return False
        rows.add(row)
        cols.add(col)
    return True

# 체스판 수 입력
n = int(input())

for _ in range(n):
    # 각 체스판에 대한 입력
    board = list(map(int, input().split()))
    num_rooks = board[0]
    rooks = [(board[i], board[i+1]) for i in range(1, len(board), 2)]
    
    # 안전 여부 확인 및 출력
    if is_safe(rooks):
        print("SAFE")
    else:
        print("NOT SAFE")