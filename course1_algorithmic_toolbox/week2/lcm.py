# Using the formulae LCM*GCD = a*b
import sys

def gcd_fast(a, b):
    # O(logab steps)
    if b == 0:
        return a
    rem = a % b
    return gcd_fast(b, rem)

def lcm(a, b):
    return int((a * b) / gcd_fast(a, b))

