cnt_line = 0

try:
    while True:
        input_line = input()
        cnt_line += 1
except EOFError:
    pass

print(cnt_line)