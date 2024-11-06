a=int(input())
i,j=1,2  #a:i, b:j
ans=0

while i!=j:
  if j**2-i**2 == a:
    ans=ans+1
  #  print('i값:',i)
    #print('j값:',j)
    j=j+1
  elif j**2-i**2 > a:
    i=i+1
  else:
    j=j+1

print(ans)  