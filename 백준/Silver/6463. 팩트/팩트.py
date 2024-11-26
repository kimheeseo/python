dp = [1]

for i in range(1, 10000):
    current = i * dp[-1]
    while current % 10 == 0:
        current /= 10
        
    current = str(int(current))
    current = current[-5:]
    #print(current)
    dp.append(int(current))

while True:
    try:
        num = int(input())
        target = dp[num]
        target = str(target)[-1]
        num = str(num)
        if len(num) == 1:
            print(f'    {num} -> {target}')
        elif len(num) == 2:
            print(f'   {num} -> {target}')
        elif len(num) == 3:
            print(f'  {num} -> {target}')
        elif len(num) == 4:
            print(f' {num} -> {target}')
    except:
        break