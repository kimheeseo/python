while True:
    try:
        # 두 개의 실수 입력 받기
        a, b = map(float, input().split())

        # 조건에 따른 출력
        if a > 0 and b > 0:
            print("Q1")
        elif a < 0 and b > 0:
            print("Q2")
        elif a < 0 and b < 0:
            print("Q3")
        elif a > 0 and b < 0:
            print("Q4")
        elif a == 0 or b == 0:
            print("AXIS")
    except EOFError:
        break  # 입력이 더 이상 없을 경우 종료