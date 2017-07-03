# Uses python3

""" Implement binary search
Input format:
First line of input contains an integer n and a sequence a0 < a1 <.. < an-1
of n pairwise distinct positive integers in increasing order. The next line
contains an integer k and k positive integers b0, b1, ... bk-1

Constraints: 1<=n,k<=10^5, 1<= ai <= 10^9 for all 0<= i < n, 1 <=bj <=10^9

Output format:
 For all i from 0 to k - 1 output an index 0<= j <= n-1 such that aj = bi or -1 if
 there is no such index.
"""

input_list = list(map(int, input().split()))
n, search_list = input_list[0], input_list[1:]

input_list = list(map(int, input().split()))
k, to_search = input_list[0], input_list[1:]

def solve(search_list, to_search):
    search_results = {}
    for element in to_search:
        if search_results.get(element, None) is not None:
            continue
        search_results[element] = binary_search_iterative(search_list, element)

    # print the results
    return [search_results.get(element) for element in to_search]

def binary_search(search_list, element, offset):
    if not search_list:
        return -1
    m = int(len(search_list) / 2)
    if search_list[m] > element:
        return binary_search(search_list[:m], element, 0)
    elif search_list[m] < element:
        return binary_search(search_list[m + 1:], element, m)
    # if its equal
    return m + offset

def binary_search_iterative(search_list, element):
    low, high = 0, len(search_list) - 1
    while low <= high:
        mid = low + int((high - low) / 2)
        if element < search_list[mid]:
            high = mid - 1
        elif element > search_list[mid]:
            low = mid + 1
        else:
            return mid
    return -1


print(' '.join(map(str, solve(search_list, to_search))))