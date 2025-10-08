import sys

def rotate_right(dx, dy):
    # clockwise 90°: (x, y) -> (y, -x)
    return dy, -dx

def rotate_left(dx, dy):
    # counter-clockwise 90°: (x, y) -> (-y, x)
    return -dy, dx

def main():
    lines = sys.stdin.read().splitlines()
    # 입력은 여러 테스트 케이스, EOF까지
    for s in lines:
        s = s.strip()
        if not s:
            continue  # 혹시 빈 줄이 섞여 있으면 무시

        x, y = 300, 420
        dx, dy = 1, 0  # initial direction: east

        print("300 420 moveto")
        # 첫 점은 항상 (310, 420)
        x += 10 * dx
        y += 10 * dy
        print(f"{x} {y} lineto")

        # 이후 문자열에 따라 회전 -> 전진
        for ch in s:
            if ch == 'A':        # clockwise
                dx, dy = rotate_right(dx, dy)
            elif ch == 'V':      # counter-clockwise
                dx, dy = rotate_left(dx, dy)
            else:
                # 문제 조건상 A/V만 오지만, 혹시 모를 예외 방지
                continue

            x += 10 * dx
            y += 10 * dy
            print(f"{x} {y} lineto")

        print("stroke")
        print("showpage")

if __name__ == "__main__":
    main()
