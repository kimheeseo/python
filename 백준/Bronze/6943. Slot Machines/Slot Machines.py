import sys
input=sys.stdin.readline

def martha_plays(quarters, machine1, machine2, machine3):
    machines = [(35, 30, machine1),  # (주기, 보상, 현재 상태)
                (100, 60, machine2),
                (10, 9, machine3)]
    plays = 0  # 총 플레이 횟수
    current_machine = 0  # 현재 플레이 중인 머신
    
    while quarters > 0:
        plays += 1  # 한 번 플레이
        quarters -= 1  # 동전 한 개 소모
        period, reward, count = machines[current_machine]
        
        count += 1  # 현재 머신의 플레이 횟수 증가
        if count == period:  # 머신이 지급 주기에 도달했을 경우
            quarters += reward  # 보상 추가
            count = 0  # 머신 상태 초기화
        
        # 업데이트한 상태를 다시 저장
        machines[current_machine] = (period, reward, count)
        
        # 다음 머신으로 이동
        current_machine = (current_machine + 1) % 3
    
    return plays

# 입력 처리
if __name__ == "__main__":
    quarters = int(input())
    machine1 = int(input())
    machine2 = int(input())
    machine3 = int(input())
    
    result = martha_plays(quarters, machine1, machine2, machine3)
    print(f"Martha plays {result} times before going broke.")
