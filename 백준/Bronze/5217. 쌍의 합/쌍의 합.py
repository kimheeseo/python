# 테스트 케이스 수 입력 받기
a = int(input())

# 각 테스트 케이스 처리
for _ in range(a):
    # 목표 숫자 입력 받기
    n = int(input())
    # 결과 출력 준비
    print(f'Pairs for {n}:', end=' ')
    
    # 쌍을 저장할 리스트
    pairs = []
    
    # 1부터 n//2까지 반복하면서 쌍 찾기
    for x in range(1, (n // 2) + 1):
        y = n - x
        if x < y:
            pairs.append(f'{x} {y}')
    
    # 리스트의 요소들을 ", "로 구분하여 출력
    print(', '.join(pairs))