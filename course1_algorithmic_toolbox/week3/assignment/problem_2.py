"""
Maximizing the value of the loot.

A thief inds much more loot than his bag can fit. Help him find
the most valuable combinations of items assuming that any
fraction of a loot item can be put into his bag.

Task:
The goal of this code problem is to implement an algorithm for
the fractional knapsack problem.

Input:
The first line of input contains the number n of items and capacity
W of the knapsack. The next n lines define the values and weights of the
items. The i-th line contains the integers vi nad wi - the value and weight of the
ith item.

Constraints:
1<=n<=10^3, 0<=W<=2*10^6, 0<=vi<2*10^6, 0<=wi<=2*10^6
Output:
Optimal maximal value of the fractions of items that fit into the knapsack.
"""



def greedy_strategy(items, max_capacity, item_details, dist=False):
    item_details_copy = sorted(item_details.copy(), key=lambda x: x[0]/x[1], reverse=True)
    capacity_left = max_capacity
    total_value = 0
    distribution = []
    # capacity can be more than the size of the items.
    while capacity_left > 0 and item_details_copy:
        value, weight = item_details_copy.pop(0)
        units_used = min(capacity_left, weight)
        total_value += (value / weight) * units_used
        distribution.append((value, units_used))
        capacity_left -= units_used
    return (round(total_value, 4), distribution) if dist else round(total_value, 4)

items, max_capacity = map(int, input().split())
item_details = []
for _ in range(items):
    item_details.append(tuple(map(int, input().split())))

print(greedy_strategy(items, max_capacity, item_details, dist=True))