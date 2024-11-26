def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    index = 1
    num = 1
    washed = []
    finished = []

    while index < len(data):
        C = int(data[index])
        D = int(data[index + 1])
        index += 2
        
        if C == 1:
            for _ in range(D):
                washed.append(num)
                num += 1
        else:
            for _ in range(D):
                finished.append(washed.pop())
    
    while finished:
        print(finished.pop())

if __name__ == "__main__":
    main()