while 1:
    a = int(input())
    if a == 0:
        break
    
    while a >= 10:  # a가 한 자리 숫자가 될 때까지 반복
        cnt = 0
        for digit in str(a):  # 각 자리 숫자를 더함
            cnt += int(digit)
        a = cnt  # 더한 값을 다시 a에 저장
    
    print(a)