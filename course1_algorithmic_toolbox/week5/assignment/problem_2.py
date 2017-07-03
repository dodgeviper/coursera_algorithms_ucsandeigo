# Uses python3

"""
Implement Knapsack without repetitions
"""

def knapsack_without_repetitions(W, items):
    weight_value_map = {0: 0}
    for i in range(len(items)):
        for w in range(1, W + 1):
            weight_value_map[w] = weight_value_map[w - 1]
            weight, value = items[i], items[i]
            if weight <= w:
                val = weight_value_map[w - weight] + value
                if weight_value_map[w] < val:
                    weight_value_map[w] = val
    return weight_value_map[W]


def knapsack(W, items):
    max_vals = [[0] * (W + 1) for x in range(len(items))]
    max_vals[0] = [items[0] if items[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(items)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]
            if items[i] <= j:
                value = max(max_vals[i - 1][j - items[i]] + items[i], value)
            max_vals[i][j] = value
    return max_vals[-1][-1]



W, n = tuple(map(int, input().split()))
items = list(map(int, input().split()))
print(knapsack(W, items))