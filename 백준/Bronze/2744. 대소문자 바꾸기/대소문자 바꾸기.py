str = input()
ans = []
for i in str:
    if 97 <= ord(i) <= 122:
        ans.append(i.upper())
    else:
        ans.append(i.lower())
print(''.join(ans))