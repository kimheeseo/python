class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def is_out_of_bound(r1, r2):
    return (r1.x2 < r2.x1 or
            r2.x2 < r1.x1 or
            r2.y2 > r1.y1 or
            r1.y2 > r2.y1)

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
r1 = Rectangle(x1, y1, x2, y2)

x1, y1, x2, y2 = map(int, input().split())
r2 = Rectangle(x1, y1, x2, y2)

# 두 사각형이 겹치지 않는 경우
if is_out_of_bound(r1, r2):
    print(0)
else:
    # 겹치는 부분의 너비와 높이 계산
    width = min(r1.x2, r2.x2) - max(r1.x1, r2.x1)
    height = max(r1.y2, r2.y2) - min(r1.y1, r2.y1)
    area = abs(width * height)
    
    # 결과 출력
    print(area)