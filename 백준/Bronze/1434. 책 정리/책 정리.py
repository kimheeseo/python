import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

# 출력
print(sum(box) - sum(book))
# 문제를 이해만 하면 쉬운 유형의 문제
# 예제 입력 3을 통해, 책의 크기가 3인 책은 2에는 들어갈수 없고

# 3에 들어가면 남은 박스 2+5
# 만일 5로 들어가면 넣은 박스의 남은 부분인 2+남은 박스 2+3=7