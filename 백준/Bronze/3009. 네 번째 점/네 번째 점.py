a,b=map(int, input().split())
c,d=map(int, input().split())
e,f=map(int, input().split())

first=[a,c,e]
second=[b,d,f]

first2=set(first)
first2=list(first2)
second2=set(second)
second2=list(second2)

for i in range(len(first2)):
  if first.count(first2[i]) == 1:
    first3=first2[i]

  if second.count(second2[i]) == 1:
    second3=second2[i]

print(first3, second3)