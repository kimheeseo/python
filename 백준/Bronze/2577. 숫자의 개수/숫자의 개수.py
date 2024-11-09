A = input()
B = input()
C = input()

got=(int(A)*int(B)*int(C))
got=list(str(got))
got.sort()

cnt=0
i=0

while 1:
  if got[i] == '0':
    cnt=cnt+1
    i=i+1
  else:
    break

  
print(cnt)

for i in range(1,10):
  print(got.count(str(i)))

