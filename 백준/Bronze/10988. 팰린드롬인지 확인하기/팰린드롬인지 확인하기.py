a=input()

count=0
for i in range(len(a)//2):
  if a[i] == a[len(a)-1-i]:
    count=count+1
  else:
  #  print('break')
    break

if count == len(a)//2:
    print(1)

else:
    print(0)
