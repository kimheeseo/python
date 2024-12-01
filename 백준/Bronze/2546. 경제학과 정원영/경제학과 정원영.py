import sys
input = sys.stdin.read
from itertools import islice

def main():
    data = input().splitlines()
    t = int(data[0])
    result = []
    idx = 1
    
    while t > 0:
        t -= 1
        idx += 1  # Skip the empty line
        n, m = map(int, data[idx].split())
        idx += 1
        arra = list(map(int, data[idx].split()))
        idx += 1
        arrb = list(map(int, data[idx].split()))
        idx += 1
        
        suma = sum(arra)
        sumb = sum(arrb)
        s = 0
        
        for value in arra:
            if value * n < suma and value * m > sumb:
                s += 1
        
        result.append(str(s))
    
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()