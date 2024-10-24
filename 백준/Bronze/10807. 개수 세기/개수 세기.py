a=int(input()) # 정수의 갯수
b=list(map(int, input().split())) #정수의 갯수만큼 값 입력
c=int(input()) # 찾으려고 하는 정수
count=0

for d in range(a):
  if b[d]== c:
    count=count+1
print(count)