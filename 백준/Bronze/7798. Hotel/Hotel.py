import sys
input=sys.stdin.readline

def find_cheapest_hotel(hotels, team):
    bed_type, people, max_per_room = team
    min_cost = float('inf')
    best_hotel = None

    for hotel in hotels:
        bed_size, capacity, rooms, cost, name = hotel
        if (bed_type == 'A' and 20 <= bed_size <= 35) or \
           (bed_type == 'B' and 36 <= bed_size <= 48) or \
           (bed_type == 'C' and 49 <= bed_size <= 62):
            rooms_needed = (people + min(max_per_room, capacity) - 1) // min(max_per_room, capacity)
            if rooms_needed <= rooms:
                total_cost = rooms_needed * cost
                if total_cost < min_cost or (total_cost == min_cost and bed_size > best_hotel[0]):
                    min_cost = total_cost
                    best_hotel = (bed_size, total_cost, name)

    return "no-hotel" if best_hotel is None else f"{best_hotel[1]} {best_hotel[2]}"

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    hotels = [input().split() for _ in range(N)]
    hotels = [(int(h[0]), int(h[1]), int(h[2]), int(h[3]), h[4]) for h in hotels]
    teams = [input().split() for _ in range(M)]
    teams = [(t[0], int(t[1]), int(t[2])) for t in teams]

    print(f"Case #{case}:")
    for team in teams:
        print(find_cheapest_hotel(hotels, team))