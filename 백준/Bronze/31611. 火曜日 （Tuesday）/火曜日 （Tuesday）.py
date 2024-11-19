import sys
input=sys.stdin.readline

def sol(x):
    if x % 7 == 2:
        return 1
    else:
        return 0
 
 
if __name__ == '__main__':
    x = int(input())
    print(sol(x))