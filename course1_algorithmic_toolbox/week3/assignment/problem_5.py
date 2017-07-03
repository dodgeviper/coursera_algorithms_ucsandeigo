# Uses python3
"""
You are organizing a funny competition for children. As a prize fund you have n candies.
You would like to use these candies for top k places in a competition with a natural
restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest value of k for
which its is possible.

Input format: single integer n 1<=n<=10^9

"""

def greedy_strategy(candies):
    candies_left = candies
    distribution = []
    prize = 0
    while candies_left > 0:
        if candies_left - (prize + 1) > prize + 1:
            prize += 1
        else:
            prize = candies_left
        candies_left -= prize
        distribution.append(str(prize))
    return len(distribution), distribution


candies = int(input())
num_prizes, distribtion = greedy_strategy(candies)
print(num_prizes)
print(' '.join(distribtion))