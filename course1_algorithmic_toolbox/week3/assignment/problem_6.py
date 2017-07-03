# python3
from functools import cmp_to_key
import random

# n = int(input())
# numbers = list(map(int, input().split()))

def compare_two_numbers(x, y):
    if x == y:
        # I don't check two same numbers till the very end.
        return x - y
    str_x = str(x)
    str_y = str(y)
    if str_x[0] != str_y[0]:
        return int(str_x[0]) - int(str_y[0])

    same = True
    max_x = len(str_x) - 1
    index_x = min(1, max_x)
    max_y = len(str_y) - 1
    index_y = min(1, max_y)
    while same:
        if str_x[index_x] != str_y[index_y]:
            return int(str_x[index_x]) - int(str_y[index_y])
        index_x = min(index_x + 1, max_x)
        index_y = min(index_y + 1, max_y)

def compare_two_numbers_improved(x, y):
    if x == y:
        return x - y
    str_x = str(x)
    str_y = str(y)
    str_xy = str_x + str_y
    str_yx = str_y + str_x
    return int(str_xy) - int(str_yx)

# Note: This algorithm is incorrect if relied on compare_two_numbers function.
def greedy_strategy(numbers):
    numbers_left = len(numbers)
    salary = ''
    # numbers_sorted = sorted(numbers.copy())
    numbers_sorted = sorted(numbers.copy(), key=cmp_to_key(compare_two_numbers), reverse=True)
    while numbers_left:
        salary += str(numbers_sorted.pop(0))
        numbers_left -= 1
    return salary

def greedy_strategy_improved(numbers):
    numbers_left = len(numbers)
    salary = ''
    # numbers_sorted = sorted(numbers.copy())
    numbers_sorted = sorted(numbers.copy(), key=cmp_to_key(compare_two_numbers_improved), reverse=True)
    while numbers_left:
        salary += str(numbers_sorted.pop(0))
        numbers_left -= 1
    return salary

def stress_testing():
    tests_pass = True
    while tests_pass:
        n = random.randint(1, 5)
        numbers = [random.randint(1, 1000) for _ in range(n)]
        print ('Input: ', numbers)
        if greedy_strategy(numbers) != greedy_strategy_improved(numbers):
            print('Test failed for: ', numbers)
            tests_pass = False
        else:
            print('Tests Pass: ', numbers)

# stress_testing()

numbers = [804, 939, 39, 396]
# Failing examples:
# [32, 323, 621]
# [32, 323]
# 804, 939, 39, 396
print(greedy_strategy(numbers))
print(greedy_strategy_improved(numbers))

# print(greedy_strategy_improved(numbers))