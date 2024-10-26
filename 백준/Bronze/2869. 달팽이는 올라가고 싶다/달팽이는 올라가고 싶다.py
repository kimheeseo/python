a,b,c=map(int,input().split())

# int(c-b) % int(a-b)가 되는 이유는 낮에 올라갔을 때, 목표치에 도달하면, 그날 미션 클리어니까
if int(c-b)%int(a-b) ==0:
  print(int(c-b)//int(a-b))
else:
  print(int(c-b)//int(a-b)+1)