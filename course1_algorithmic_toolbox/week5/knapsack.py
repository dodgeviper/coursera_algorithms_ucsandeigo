"""TV commercial placement.
Select a set of TV commercials (each commercial has duration and cost) so that
the total revenue is maximal while the total length does not exceed the length
of the available time slot.
"""


"""
Optimizing data center performance.

Purchase computers for a data center to a achieve the maximal performance under
limited budget.
"""


"""When repetitions are allowed"""
def knapsack(W, items):
    weight_value_map = {0: 0}
    for w in range(1, W + 1):
        weight_value_map[w] = 0
        for weight, value in items:
            if weight <= w:
                val = weight_value_map[w - weight] + value
                if val > weight_value_map[w]:
                    weight_value_map[w] = val
    return weight_value_map[W]

W = 10
items = [(6, 30), (3, 14), (4, 16), (2, 9)]
print(knapsack(W, items))


"""When Repetitions are not allowed"""
def knapsack_without_repetitions(W, items):
    weight_value_map = {0: 0}
    for i in range(len(items)):
        for w in range(1, W):
            weight_value_map[w] = weight_value_map[w -1]
            weight, value = items[i]
            if weight <= w:
                val = weight_value_map[w - weight]  + value
                if weight_value_map[w] < val:
                    weight_value_map[w] = val
    return weight_value_map[W]

W = 10
items = [(6, 30), (3, 14), (4, 16), (2, 9)]
print(knapsack_without_repetitions(W, items))