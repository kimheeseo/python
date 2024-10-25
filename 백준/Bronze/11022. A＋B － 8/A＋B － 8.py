a=int(input()) #테스트 케이스의 갯수

for aa in range(a):
    b,c = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(aa+1, b,c,b+c))