import sys
input_data = sys.stdin.read().splitlines()
a=set()
c=set()
for b in input_data:
    if b == '000-00-0000':
        break
    if b in a :
        c.add(b)
    else :
        a.add(b)
c=sorted(c)
for i in c:
    print(i)