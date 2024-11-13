import sys
input = sys.stdin.readline

a, b, c, d, e = map(int, input().split())
current_pulse = b
total_time = 0
exercise_time = 0

# 최대 맥박이 초기 맥박보다 작거나 증가할 수 없는 경우
if b + d > c:
    print(-1)
else:
    while exercise_time < a:
        if current_pulse + d <= c:
            # 운동할 수 있는 경우
            current_pulse += d
            exercise_time += 1
        else:
            # 운동할 수 없으면 휴식
            current_pulse = max(b, current_pulse - e)
        total_time += 1

    print(total_time)