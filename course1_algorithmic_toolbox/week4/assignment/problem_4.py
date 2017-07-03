# Uses python3

"""How close a data is to being sorted
An inversion of sequence a0, a1, .. an-1 is a pair of indices 0<= i < j< n
such that ai < aj. The number of inversion of a sequence in some sense measures
how close the sequence is to being sorted. For example, a sorted (in non-decreasing
order) sequence contains no inversions at all, while in a sequence sorted in descending
order any two elements constitute an inversion (for a total of n(n - 1)/ 2 inversions)

Task: the goal is to count the number of inversions of a given sequence.

Input format: First line contains an integer n, the next one contains a sequence of
integers a0, a1.. an-1

Constraints:
1<= n < 10^5, 1 <= ai <= 10^9 for all 0 <= i < n

Output:
The number of inversions of the sequence.
"""

inversion_count = [0]

def merge(a, b):
    d = list()
    index_a, index_b = 0, 0
    len_a = len(a)
    while index_a < len(a) and index_b < len(b):
        el_a = a[index_a]
        el_b = b[index_b]
        if el_a <= el_b:
            d.append(el_a)
            index_a += 1
        else:
            d.append(el_b)
            index_b += 1
            inversion_count[0] += (len_a - index_a)
    d.extend(a[index_a:])
    d.extend(b[index_b:])
    return d


def merge_sort(n):
    if len(n) == 1:
        return n
    mid = int(len(n) / 2)
    left_half = merge_sort(n[:mid])
    right_half = merge_sort(n[mid:])
    return merge(left_half, right_half)

#
# def counting_inversions_naive(input_list):
#     count = 0
#     for i in range(len(input_list)):
#         for j in range(i+1, len(input_list)):
#             if input_list[i] > input_list[j]:
#                 count += 1
#     return count
#
# import random
# def stress_testing():
#     while True:
#         n = random.randint(1, 3)
#         input_list = [random.randint(1, 100) for _ in range(n)]
#         count_naive = counting_inversions_naive(input_list)
#         inversion_count[0] = 0
#         merge_sort(input_list)
#         count_eff = inversion_count[0]
#         if count_naive != count_eff:
#             print('Failed')
#             print(n)
#             print(input_list)
#             print('count naive; ', count_naive)
#             print('optimized: ', count_eff)
#             break
#
#
#
# stress_testing()
#
n = input()
input_list = list(map(int, input().split()))
# # inversions = []
# # n = 6
# # input_list = [9, 8, 7, 3, 2, 1]
merge_sort(input_list)
print(inversion_count[0])
# print(counting_inversions_naive(input_list))