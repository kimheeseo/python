a, b = input().split()
b = int(b)

sum = 0
for jj in range(len(a)):
    c = a[jj]
    if c.isdigit():
        inter = int(c)
    else:
        inter = ord(c) - ord('A') + 10
    sum += inter * b**(len(a) - jj - 1)

print(sum)