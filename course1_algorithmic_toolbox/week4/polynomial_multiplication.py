
def polynomial_naive(A, B):
    product = [0 for _ in range(2*len(A) - 1)]
    for i in range(len(A)):
        for j in range(len(A)):
            product[i + j] += A[i] * B[j]
    return product

print(polynomial_naive([3, 4], [1, 2]))

# Karatsuba multiplication
