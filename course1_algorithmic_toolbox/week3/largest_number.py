"""
What is the largest number that consists of digits 3, 9, 5, 9, 7, 1?
Use all the digits
"""

def naive_largest_number(list_of_digits):
    """ Sort the list in descending order and join them
    O(nlogn) - complexity of sorting algorithm.
    :param list_of_digits:
    :return:
    """
    # Sort the list
    list_of_digits = sorted(list_of_digits, reverse=True)
    return ''.join(map(str, list_of_digits))


def approach_2(list_of_digits):
    number_of_digits = len(list_of_digits)
    previous = -1
    for index in range(number_of_digits):
        if previous == -1:
            previous = list_of_digits[index]
        if previous < list_of_digits[index]:
            list_of_digits[index - 1], list_of_digits[index] = list_of_digits[index], previous
            previous = list_of_digits[index]
    return ''.join(map(str, list_of_digits))

def greedy_strategy(list_of_digits):
    """
    Find the maximum of the list and append it in the number and then remove that
    from the list.
    :param list_of_digits: list
    :return:
    """
    number = []
    while len(list_of_digits):
        maximum = -1
        max_index = -1
        for index in range(len(list_of_digits)):
            if maximum < list_of_digits[index]:
                maximum = list_of_digits[index]
                max_index = index
        number.append(maximum)
        list_of_digits.pop(max_index)
    return ''.join(map(str, number))


print(naive_largest_number([3, 9, 5, 9, 7, 1]))
print(greedy_strategy([3, 9, 5, 9, 7, 1]))


"""
Variation: Given 23<= x <= 73. Find the largest x which has the maximum products of its digits.
"""

