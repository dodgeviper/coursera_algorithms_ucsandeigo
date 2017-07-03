def max_pairwise_product(numbers):
    result = 0
    input_size = len(numbers)
    for i in range(0, input_size):
        for j in range(i+1, input_size):
            if numbers[i] * numbers[j] > result:
                result = numbers[i] * numbers[j]
    return result


def max_pairwise_product_fast(numbers):
    maximum_number = max(numbers) # O(n)
    numbers.remove(maximum_number) # O(n)
    second_maximum_number = max(numbers) # O(n)
    return maximum_number * second_maximum_number

input_size = int(input())
numbers = [int(number) for number in input().split()]
assert input_size == len(numbers)
print(max_pairwise_product_fast(numbers))