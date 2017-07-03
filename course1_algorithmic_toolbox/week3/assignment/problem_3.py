# python3
"""
Maximizing Revenue in Online ad placement.
You have n ads to place on a popular internet page. For each
ad, you know how much is the advertiser willing to pay for one
click on this ad. You have set up n slots on your page and
estimated the expected number of clicks per day for each slot.
Now your goal is to distribute the ads among the slots to maximize
the total revenue.

Task: Given two sequences a1, a2, ... an (ai is the profit per click of the ith
 ad) and b1, b2.. bn (bi is the average  number of clicks per day of the i-th slot),
 we need to partition them into n pair (ai, bi) such that the sum of their products
 is maximized.

Input format: 1<= n <= 10^3, -10^5<= ai, bi <= 10^5

Output the maximum value of Sum(ai, ci) where c1, c2/.. cn is a permuation of b1, b2..bn.
"""

placements = int(input())
profits = map(int, input().split())
clicks = map(int, input().split())

def greedy_strategy(placements, profits, clicks):
    profits = sorted(profits, reverse=True)
    clicks = sorted(clicks, reverse=True)
    total_revenue = 0
    for _ in range(placements):
        total_revenue += profits.pop(0) * clicks.pop(0)
    return total_revenue


print(greedy_strategy(placements, profits, clicks))