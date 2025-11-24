def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_profit = 0.0

    for weight, value in items:
        if capacity == 0:
            break
        
        if weight <= capacity:
            # take full item
            total_profit += value
            capacity -= weight
        else:
            # take fractional part
            fraction = capacity / weight
            total_profit += fraction * value
            capacity = 0
    
    return total_profit


items = [(10, 60), (20, 100), (30, 120)]
capacity = 50

result = fractional_knapsack(items, capacity)
print("Maximum Profit =", result)
