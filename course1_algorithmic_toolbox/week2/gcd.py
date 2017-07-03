def gcd_naive (a, b):
    best = 0
    for d in range(1, a+b):
        if d % a == 0 and d % b == 0:
            best = d
    return best

def gcd_fast(a, b):
    # O(logab steps)
    if b == 0:
        return a
    rem = a % b
    return gcd_fast(b, rem)


#print (gcd_naive(128391231123, 312311231231))
a = int(input())
b = int(input())
print(gcd_fast(a, b))