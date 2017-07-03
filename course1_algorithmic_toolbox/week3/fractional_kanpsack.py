"""
Long hike problem.
Knapsack problem: Fractional knapsack.
Input:
Weights w1,.. wn and values v1, ... vn of n items capacity W

Output:
Maximum total value of fractions of items that fit
into a bag of capacity W.
"""


"""
Example: Three items: (fractions are allowed)
$20 - 4 weight
$18 - 3 weight
$14 - 2 weight

Fill in the knapsack with max capacity of 7 units to maximize the value.

Solution:
$20 - 4 weight - $5/unit
$18 - 3 weight - $6/unit
$14 - 2 weight - $7/unit

Safe move: Fill as much of item which has maximum value/unit and
then move on to the next one.
"""

def greedy_strategy(items, maximum_capacity):
    """
    Complexity is O(n^2) :
    n times for selection
    and O(n) for selecting the max items
    :param items: of the type tuple (w, v)
    :param maximum_capacity:
    :return:
    """
    def max_units_value():
        max_per_unit_value = 0
        max_index = -1
        for index in range(len(input_items_copy)):
            cost, unit = input_items_copy[index]
            if max_per_unit_value < cost/unit:
                max_per_unit_value = cost/unit
                max_index = index
        return input_items_copy.pop(max_index)

    input_items_copy = items.copy()
    capacity_left = maximum_capacity
    max_cost = 0
    item_split = []
    while capacity_left > 0:
        cost, units = max_units_value()
        units_used = min(capacity_left, units)
        capacity_left = capacity_left - units_used
        max_cost += (cost/units) * units_used
        item_split.append((cost, units_used))
    return max_cost, item_split

def greedy_strategy_improved(items, maximum_capacity):
    """
    O(nlogn) complexity due to sorting to calculate the maximum.
    and n operations for the actual algo.
    :param items:
    :param maximum_capacity:
    :return:
    """
    input_items_copy = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    capacity_left = maximum_capacity
    max_cost = 0
    item_split = []
    while capacity_left > 0 or input_items_copy:
        cost, units = input_items_copy.pop(0)
        units_used = min(capacity_left, units)
        capacity_left = capacity_left - units_used
        max_cost += (cost/units) * units_used
        item_split.append((cost, units_used))
    return max_cost, item_split


# Should print out 42.0
print(greedy_strategy([(20,4), (18,3), (14,2)], 7))
print(greedy_strategy_improved([(20,4), (18,3), (14,2)], 7))

print(greedy_strategy_improved([(20, 20), (10, 5), (20, 4)], 10))