import sys
input=sys.stdin.readline

m=int(input())
cup=[0,1,2,3]

for i in range(m):
    x,y=map(int, input().split())
    cup[x],cup[y]=cup[y],cup[x]
print(cup.index(1))
# 공이 들어있는 컵의 번호를 출력한다.: 1번째 컵의 아래에 공을 넣는다.