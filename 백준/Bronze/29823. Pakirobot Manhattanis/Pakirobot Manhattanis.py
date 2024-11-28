def min_steps_to_warehouse(steps):
    x, y = 0, 0
    for step in steps:
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
    
    return abs(x) + abs(y)

# Read input
N = int(input())
steps = input().strip()

# Calculate and print the result
print(min_steps_to_warehouse(steps))