a=int(input()) #테스트 케이스의 개수

for aa in range(a):
    b,c=map(int, input().split())
    print('Case #%d: %d' %(aa+1, c+b))