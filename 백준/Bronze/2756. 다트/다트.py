import math

class Position:
    """다트의 x, y 좌표를 저장하는 클래스"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_score(player):
    """플레이어의 점수를 계산하는 함수"""
    sum_score = 0
    for p in player:
        distance = math.sqrt(p.x ** 2 + p.y ** 2)  # 원점 (0, 0)에서의 거리 계산
        # 거리 범위에 따라 점수 결정
        if distance <= 3:
            sum_score += 100
        elif distance <= 6:
            sum_score += 80
        elif distance <= 9:
            sum_score += 60
        elif distance <= 12:
            sum_score += 40
        elif distance <= 15:
            sum_score += 20
    return sum_score

def main():
    # 테스트 케이스 수 입력
    T = int(input())
    
    for _ in range(T):
        player1 = []  # 첫 번째 플레이어의 다트 위치
        player2 = []  # 두 번째 플레이어의 다트 위치

        # 6개의 점수를 입력받기
        inputs = list(map(float, input().split()))
        for j in range(6):
            x = inputs[j * 2]     # x 좌표
            y = inputs[j * 2 + 1] # y 좌표
            if j < 3:
                player1.append(Position(x, y))  # 첫 번째 플레이어의 위치 추가
            else:
                player2.append(Position(x, y))  # 두 번째 플레이어의 위치 추가

        # 각 플레이어 점수 계산
        player1_score = get_score(player1)
        player2_score = get_score(player2)

        # 결과 출력
        print(f"SCORE: {player1_score} to {player2_score}, ", end="")
        if player1_score == player2_score:
            print("TIE.")
        elif player1_score > player2_score:
            print("PLAYER 1 WINS.")
        else:
            print("PLAYER 2 WINS.")

if __name__ == "__main__":
    main()