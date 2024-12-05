import sys

def main():
    input = sys.stdin.readline
    # 입력받은 데이터 처리
    line = input().strip().split()
    N = int(line[0])  # 인원 수 N
    
    # 승리 조건에 대한 처리 (마지막 게임 승리자가 최종 승자)
    result = line[1][-1]  # 마지막 문자 추출
    print(result)

if __name__ == "__main__":
    main()