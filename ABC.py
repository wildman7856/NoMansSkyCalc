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

def combinations(lst, n): 
    """recursively creates a list of unique combinations"""
    if n == 0: 
        return [[]] 
      
    output = [] 
    for i in range(0, len(lst)): 
          
        fist_selection = lst[i] 
        remaining_items = lst[i + 1:] 
          
        for next_selection in combinations(remaining_items, n-1): 
            output.append([fist_selection]+next_selection) 
              
    return output

# Use combinations from itertools to create all possible combinations (selecting 5)

# unique_combinations = combinations(list(ship_data.keys()), 5)

unique_combinations = []
for number_of_ships in range(6):
    for combo in combinations(list(ship_data.keys()), number_of_ships):
        unique_combinations.append(combo)

# filter the combinations by calculating the total of the scores for each ship in the combination

#filtered_combinations = [combo for combo in unique_combinations if sum([ship_data[ship]['score'] for ship in combo]) <= target]
# Converted list comprehension into nested for loops -- easier to translate into VBA
filtered_combinations = []
for combo in unique_combinations:
    current_combo_total_score = 0
    for ship in combo:
        current_combo_total_score += ship_data[ship]['score']
    if current_combo_total_score >= target:
        filtered_combinations.append(combo)


def calculate_fuel(ships):
    """Placeholder function to allow for future fuel consumption updates"""
    return sum([ship_data[ship]['fuel'] for ship in ships])

results = []
for combo in filtered_combinations:
    score = sum([ship_data[ship]['score'] for ship in combo])
    fuel = calculate_fuel(combo)
    results.append({
        "ships":combo,
        "score":score,
        "fuel":fuel
    })

results.sort(key = lambda x: x['fuel'])

for result in results:
    print(result)





    
    
