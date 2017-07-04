# Uses python 3.

"""Goal is to add parentheses to a given arithmetic expression to maximize its value.

Find the maximum value of an arithmatic expression by specifying the order of applying its
arithmetic operations using additional parentheses.

Input:
The only line of the input contains a string s of  length 2n+1 for some n, with symbols s0,s1,.. sn.
Each symbol at an even possible position of s is a digit (that is, an integer from 0 to 9) while
each symbol at an odd position is one of the three operations {+, -, *}

Constraints: 1 <= n<= 14 (hence the string contains at most 29 symbols)

Output Format:
Output the maximum possible value of the given arithmetic expression among different orders of applying
arithmetic operations.
"""

import math

def Parentheses(s):
    digits = [d for i, d in enumerate(s) if i % 2 == 0]
    operations = [ops for i, ops in enumerate(s) if i % 2 != 0]
    m = [[0] * len(digits) for _ in range(len(digits))]
    M = [[0] * len(digits) for _ in range(len(digits))]

    def operate(a, op, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        else:
            raise ValueError('Unsupported operation: ', op)

    def MinAndMax(i, j):
        min1, max1 = math.inf, -math.inf
        for k in range(i, j):
            a = operate(M[i][k], operations[k], M[k + 1][j])
            b = operate(M[i][k], operations[k], m[k + 1][j])
            c = operate(m[i][k], operations[k], M[k + 1][j])
            d = operate(m[i][k], operations[k], m[k + 1][j])
            min1 = min(min1, a, b, c, d)
            max1 = max(max1, a, b, c, d)

        return min1, max1

    for i in range(len(digits)):
        m[i][i] = int(digits[i])
        M[i][i] = int(digits[i])

    for d in range(1, len(digits)):
        for i in range(len(digits) - d):
            j = i + d
            m[i][j], M[i][j] = MinAndMax(i, j)
    return M[0][len(digits)-1]



s = input()
print(Parentheses(s))