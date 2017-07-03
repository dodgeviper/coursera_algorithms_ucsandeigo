import random
from math import sqrt

class Fibonacci(object):

    def __init__(self):
        self.fib = {0:0, 1:1}

    def fibonacci(self, n):
        if n <=1 :
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_fast(self, n):
        if self.fib.get(n):
            return self.fib.get(n)
        self.fib[n] = self.fibonacci_fast(n - 1) + self.fibonacci_fast(n - 2)
        return self.fib[n]

    def fibonacci_fast_iterative(self, n):
        if n <= 1:
            return n
        fib = {0: 0, 1: 1}
        for x in range(2, n + 1):
            fib[x] = fib[x - 1] + fib[x - 2]
        return fib[x]


    def fibonacci_last(self, n):
        fib_last = {0: 0, 1: 1}
        for i in range(2, n + 1):
            fib_last[i] = (fib_last[i - 1] + fib_last[i - 2]) % 10
        return fib_last[n]


    def fibonacci_huge(self, n, m):
        # Pisano periods: Fibonacci series modulo m repeats
        def pisano_period(m):
            a, b = 0, 1
            c = a + b
            for x in range(m*m):
                c = (a + b) % m
                a, b = b, c
                if a == 0 and b == 1:
                    return x - 1

        remainder = n % pisano_period(m)
        a1, b1 = 0, 1
        c1 = (a1 + b1)
        for x in range(2, remainder + 1):
            c1 = (a1 + b1) % m
            a1, b1 = b1, c1
        return c1 % m

    def fibonacci_sum_naive(self, n):
        """Find the last digit of a sum of the first n Fibonacci numbers.

        Given an integer n, find the last digit of the sum F0+F1+...+FN

        :param n: integer. Between 0 to 10^14
        :return: integer. last digit of the sum.
        """
        a, b = 0, 1
        c = a + b
        sum = c
        for i in range(2, n + 1):
            c = a + b
            sum = sum + c
            a, b = b, c
        return sum % 10

    def calculate_fibonacci_number(self, n):
        sqrt_five = sqrt(5)
        return (pow((1 + sqrt_five), n) - pow((1 - sqrt_five), n)) / (pow(2, n) * sqrt_five)

    def fibonacci_sum_fast(self, n):
        return (self.calculate_fibonacci_number(n + 2) - 1) % 10


    def fibonacci_partial_sum(self, n, m):
        return int((self.calculate_fibonacci_number(n + 2) - self.calculate_fibonacci_number(m + 1)) % 10)

n = int(input())
m = int(input())
fib = Fibonacci()
# print(fib.fibonacci_sum_fast(n))
print(fib.fibonacci_partial_sum(n, m))