grad=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D+','D0','D-','F']
scor=[4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]

a = input().strip()
b=grad.index(a)
print(scor[b])
