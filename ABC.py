from itertools import combinations
target = 20

# Store data in a dictionary so it can be called by name
ship_data = {
    "a":{"score":100, "fuel":4},
    "b":{"score":1, "fuel":5},
    "c":{"score":2, "fuel":6},
    "d":{"score":3, "fuel":7},
    "e":{"score":4, "fuel":8},
    "f":{"score":5, "fuel":9},
    "g":{"score":6, "fuel":10},
}

# Use combinations from itertools to create all possible combinations (selecting 5)
unique_combinations = combinations(ship_data.keys(), 5)

# filter the combinations by calculating the total of the scores for each ship in the combination
filtered_combinations = [combo for combo in unique_combinations if sum([ship_data[ship]['score'] for ship in combo]) <= target]

# print results
for combo in filtered_combinations:
    score = sum([ship_data[ship]['score'] for ship in combo])
    fuel = sum([ship_data[ship]['fuel'] for ship in combo])
    print(f"\nShips: {combo}")
    print(f"\tScore: {score}")
    print(f"\tFuel: {fuel}")






    
    
