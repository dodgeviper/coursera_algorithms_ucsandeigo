# Uses python3

"""Improving Quick Sort
The goal in this problem is to redesign a given implementation of the randomized
quick sort algorithm so that it works fast even on sequences containing many equal
elements.

Task: To force the given implementation of the quick  sort algorithm to efficiently
process sequences with few unique elements, your goal is to replace 2-way partition
with a 3-way partition. That is your new partition procedure should partition
the array into three parts < x part, = x part and > x part.

Input: The first line of the input contains an integer n. The next line contains a
sequence of n integers a0, a1.... an-1
Constraints:
1<= n <= 10^5, 1< ai <= 10^9, for all 0<=i < n
Output:
Output the sequence in non-decreasing order.
"""
n = input()
input_list = list(map(int, input().split()))


def partition(input_list, pivot):
    less, equal, greater = [], [], []
    for element in input_list:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[0]
    less, equal, greater = partition(input_list, pivot)
    return quick_sort(less) + equal + quick_sort(greater)

print(' '.join(map(str, quick_sort(input_list))))
#print(input_list)