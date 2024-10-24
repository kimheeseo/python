a=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count=0

b=list(input()) # 전화번호
for i in range(len(b)):
  for j in range(len(a)):
    if b[i] in a[j]:
      count=count+j+3
      break
print(count)