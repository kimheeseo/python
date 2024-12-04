# 10진수에서 다른 진수로 변환하는 코드
a=10 # 10진수
aa=a
b=[]
c=7
while 1:
  if a<c:
    b.append(a%c)
    break
  b.append(a%c)
  a=a//c

# 진수 표현
d=[]
for j in range(len(b)-1,-1,-1):
  d.append(b[j])
print('10진수 표현:%d' %aa)
print('%d 진수 표현:' %c, end="")
for i in range(len(d)):
  print(d[i],end="")
