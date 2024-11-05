a=0
for i in range(0,5):
  b=int(input())
  if b<40:
    b=40
  a=b+a
print(int(a/5))