"""Convert string to number."""


def my_int(num_str, radix, allowed_symbols):
    number = 0
    # It only handles negative number for base 10.
    negative = num_str[0] == '-' and radix == 10
    num_str = num_str[negative:]
    factor = 1
    for index, char in enumerate(num_str[::-1]):
        # Handles decimal only for base 10
        if char == '.' and radix == 10:
            number = number/factor
            factor = 1
            continue

        if allowed_symbols.get(char) is None:
            raise ValueError('invalid string found %s' % char)

        number += allowed_symbols.get(char) * factor
        factor *= radix
    return number if not negative else -number


base_10_allowed_symbols = {'0': 0,
                           '1': 1,
                           '2': 2,
                           '3': 3,
                           '4': 4,
                           '5': 5,
                           '6': 6,
                           '7': 7,
                           '8': 8,
                           '9': 9}


base_2_symbols = {'0': 0, '1': 1}
base_16_symbols = {'0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'A': 10,
                   'B': 11,
                   'C': 12,
                   'D': 13,
                   'E': 14,
                   'F': 15}
# tests
print(my_int('1234', 10,  base_10_allowed_symbols))
print(my_int('1234.787', 10,  base_10_allowed_symbols))
# print(my_int('as123'))
# print(my_int('1234a'))

print(my_int('-1234', 10, base_10_allowed_symbols))
print(my_int('101', 2, base_2_symbols))
print(my_int('AA', 16, base_16_symbols))