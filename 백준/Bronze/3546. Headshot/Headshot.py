import sys

def main():
    str = sys.stdin.readline().strip()

    cnt = 0
    cnt2 = 0
    for i in range(len(str)):
        if str[i] == '0':
            cnt += 1
            if i > 0 and str[i - 1] == '0':
                cnt2 += 1

    if str[0] == '0' and str[-1] == '0':
        cnt2 += 1

    if cnt * cnt == len(str) * cnt2:
        print("EQUAL")
    elif cnt * cnt < len(str) * cnt2:
        print("SHOOT")
    else:
        print("ROTATE")

if __name__ == "__main__":
    main()

