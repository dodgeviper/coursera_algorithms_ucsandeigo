# Uses python3

"""Majority element:
Majority rule is a decision rule that selects the alternative which has a majority,
that is, more than half the votes.
Given a sequence of elements a1, a2,... an you would like to check whether it contains
an element that appears more than n/2 times.

Input:
 THe first line contains an integer n, the next contains a sequence of n non-negative
 integers a0, a1... an-1
Constraints: 1<= n <= 10^5, 0<= ai <= 10^9 for all 0<= i < n
"""

n = input()
input_list = list(map(int, input().split()))

def has_majority_element(input_list):
    element_dict = {}
    majority = int(len(input_list) / 2)
    for element in input_list:
        element_dict[element] = element_dict.get(element, 0) + 1
        if element_dict[element] > majority:
            return 1
    return 0

print(has_majority_element(input_list))