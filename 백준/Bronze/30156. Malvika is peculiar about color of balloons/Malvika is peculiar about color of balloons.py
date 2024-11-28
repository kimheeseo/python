def min_flips(s):
    return min(s.count('a'), s.count('b'))

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    s = input().strip()
    print(min_flips(s))