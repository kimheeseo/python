def simulate_spinner(initial_state, button_presses):
    wheels = list(map(int, initial_state))
    
    for button in button_presses:
        for i, move in enumerate(button):
            wheels[i] = (wheels[i] + int(move)) % 10
    
    return ''.join(map(str, wheels))

# 입력 처리
initial_state = input().strip()
button_presses = []

while True:
    try:
        button = input().strip()
        if not button:
            break
        button_presses.append(button)
    except EOFError:
        break

# 시뮬레이션 실행 및 결과 출력
result = simulate_spinner(initial_state, button_presses)
print(result)