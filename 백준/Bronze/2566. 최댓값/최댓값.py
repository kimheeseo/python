max_row=0
max_col=0
max_b=-1

for i in range(9):
    b=list(map(int,input().split()))
    for j in range(9):
        if b[j]>max_b:
            max_b=b[j]
            max_row=i+1
            max_col=j+1

print(max_b)
print(max_row, max_col)