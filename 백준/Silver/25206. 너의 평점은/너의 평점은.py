rating=['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade=[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total1=0
total2=0

for i in range(20):
  a,b,c=input().split()
  if c in rating:
    total1=total1+float(b)*grade[rating.index(c)]
    total2=total2+float(b)
print(total1/total2)