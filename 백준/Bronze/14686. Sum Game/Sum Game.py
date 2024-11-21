def main():
    N = int(input())
    
    # Create the prefix sum array for the Swifts team
    games = [0] * N
    swift_scores = list(map(int, input().split()))
    
    for i in range(N):
        if i == 0:
            games[i] = swift_scores[i]
        else:
            games[i] = games[i - 1] + swift_scores[i]
    
    # Calculate the prefix sum for the Semaphores team
    semaphore_scores = list(map(int, input().split()))
    prefixsum = 0
    ans = 0
    
    for i in range(N):
        prefixsum += semaphore_scores[i]
        if prefixsum == games[i]:
            ans = i + 1  # If prefix sums are equal, update the answer
    
    print(ans)

if __name__ == "__main__":
    main()