c=int(input())

a=[i for i in range (1,100001)]
b='0'
for i in a:
  b=b+str(i)
print(b.index(str(c)))