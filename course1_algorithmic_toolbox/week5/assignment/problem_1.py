# Uses python3
"""Primitive Calculator
You are given a primitive calculator that can perform the following 3 operations on
number x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a positive
integer n, find the minimum number of operations needed to obtain the number n from x.

Task: Given an integer n compute the minimum number of operations needs to obtain the
number n starting from number 1.

Input Format:
 The input consists of single integer 1 <= n <= 10^6

Output format:
In the first line output the  minimum number k of operations needed to get n from 1.
In the second line output the sequence of intermediate numbers. That is the second
line should contain the positive integers a0, a1.... ak-1 such that a0= 1, ak-1 =n
and for all 0<= i < k- 1, ai+1 is equal to either ai + 1, 2ai or 3ai. If there are
many such sequences, output any one of them.
"""
import math



""" This is the greedy approach which is incorrect"""
opreations = [0]
def primitive_calculator_incorrect(n, operations):
    if n == 1:
        return 1

    operations[0] += 1

    if n % 3 == 0:
        print(n/3)
        return primitive_calculator_incorrect(n/3, operations)

    if n % 2 == 0:
        print(n/2)
        return primitive_calculator_incorrect(n/2, operations)
    print(n - 1)
    return primitive_calculator_incorrect(n - 1, operations)



"""Correct approach"""

def primitive_calculator(n):
    ops = {1: 0, 2: 1, 3: 1}

    def count(n):
        if ops.get(n) is not None:
            return ops[n]

        count_1 = count(n - 1) + 1
        count_3 = (count(n/3) + 1) if n % 3 == 0 else math.inf
        count_2 = (count(n/2) + 1) if n % 2 == 0 else math.inf


        min_count = min(count_3, count_2, count_1)
        ops[n] = min_count
        return ops[n]

    count(n)
    return ops[n]


def primitive_calculator_iterative(n):
    hop_count = [0] * (n + 1)

    # Path from 1 to 1 is 1.
    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_count[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_count[i] = min_hops + 1

    # ptr points to current position of hop_count.
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        # The list contains next hop candidates.
        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        # Choose from the candidates whose hop count is the least.
        ptr = min(
            [(c, hop_count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)


n = int(input())
sequence = list(primitive_calculator_iterative(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")



# n = int(input())
#print(primitive_calculator(n))
# primitive_calculator_iterative(n)
# print(primitive_calculator_incorrect(n, opreations))
# print(opreations[0])
