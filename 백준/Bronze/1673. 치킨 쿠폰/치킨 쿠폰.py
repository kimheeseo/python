while True:
    try:
        # 치킨 수와 필요한 쿠폰 수를 입력 받음
        a, b = map(int, input().split())
        
        # 초기 치킨 개수와 쿠폰 개수
        total_chicken = a
        coupons = a
        
        # 쿠폰을 사용할 수 있을 때까지 반복
        while coupons >= b:
            # 치킨 추가로 얻을 수 있는 개수 계산
            new_chickens = coupons // b
            total_chicken += new_chickens
            
            # 남은 쿠폰 계산 (새로운 쿠폰 + 사용하고 남은 쿠폰)
            coupons = new_chickens + (coupons % b)
        
        print(total_chicken)
    
    except EOFError:
        break