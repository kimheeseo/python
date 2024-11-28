# Read input
N, H = map(int, input().split())
ride_heights = list(map(int, input().split()))

# Count rides Carlitos can go on
accessible_rides = sum(1 for height in ride_heights if H >= height)

# Print the result
print(accessible_rides)