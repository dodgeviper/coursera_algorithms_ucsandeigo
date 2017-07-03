"""
Task: The goal in this problem is to find the minimum number of coins needed to change
the input value (integer) into coins with denominations of 1, 5, 10.

Input format: single integer m. (1<=m<=10^3)
Output: minimum number of coins with denominations 1, 5, 10 that changes m.
"""

def greedy_strategy(m, print_dist=False):
    denominations = [10, 5, 1] # assumption is denomination is sorted.
    total_coins = 0
    change_left = m
    coin_distribution = []
    while change_left > 0:
        coin_value = denominations.pop(0)
        no_of_coins = int(change_left/coin_value)
        coin_distribution.append((coin_value, no_of_coins))
        total_coins += no_of_coins
        change_left -= coin_value * no_of_coins
    return (total_coins, coin_distribution) if print_dist else total_coins


m = int(input())
print(greedy_strategy(m, print_dist=True))
#print(greedy_strategy(1000))
assert 100 == greedy_strategy(1000)
assert 1 == greedy_strategy(1)