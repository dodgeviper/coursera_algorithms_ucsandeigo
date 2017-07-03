# Uses python3
"""Finding closest pair of points
Your goal is to find the closest pair of points among the given n points.
This is a basis primitive computational gelometry having application in for example
graphics, computer vision, traffic-control systems.

Task:
Given n points on a plane, find the smallest distance between a pair of two points.
Recall that the distance between points (x1, y1) and x2, y2 is equal to
((x1 - x2)**2 + (y1 - y2)**2)**0.5

Input format:
The first line contains the number of n points. Each of the following n lines defines a
point xi, yi

Constraints: 1<= n <= 10^5, -10^9 <= xi, yi <= 10^9 are integers

Output format:
Output the minimum distance. The absolute value of the difference between the anser of your
program and the optimal value should be at most 10^-3. To ensure this, the output your answer
with atleast 4 digits after the decimal point.
"""

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def minimum_distance(points):
    if len(points) < 2:
        return math.inf
    best_pair = closestpair(points)
    return distance(best_pair[0], best_pair[1])

def closestpair(L):

    def square(x):
        return x * x

    def sqdist(p, q):
        return square(p[0] - q[0]) + square(p[1] - q[1])

    # Work around ridiculous Python inability to change variables in outer scopes
    # by storing a list "best", where best[0] = smallest sqdist found so far and
    # best[1] = pair of points giving that value of sqdist.  Then best itself is never
    # changed, but its elements best[0] and best[1] can be.
    #
    # We use the pair L[0],L[1] as our initial guess at a small distance.
    best = [sqdist(L[0], L[1]), (L[0], L[1])]

    # check whether pair (p,q) forms a closer pair than one seen already
    def testpair(p, q):
        d = sqdist(p, q)
        if d < best[0]:
            best[0] = d
            best[1] = p, q

    # merge two sorted lists by y-coordinate
    def merge(A, B):
        i = 0
        j = 0
        while i < len(A) or j < len(B):
            if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
                yield A[i]
                i += 1
            else:
                yield B[j]
                j += 1

    # Find closest pair recursively; returns all points sorted by y coordinate
    def recur(L):
        if len(L) < 2:
            return L
        split = int(len(L) / 2)
        splitx = L[split][0]
        L = list(merge(recur(L[:split]), recur(L[split:])))

        # Find possible closest pair across split line
        # Note: this is not quite the same as the algorithm described in class, because
        # we use the global minimum distance found so far (best[0]), instead of
        # the best distance found within the recursive calls made by this call to recur().
        # This change reduces the size of E, speeding up the algorithm a little.
        #
        E = [p for p in L if abs(p[0] - splitx) < best[0]]
        for i in range(len(E)):
            for j in range(1, 8):
                if i + j < len(E):
                    testpair(E[i], E[i + j])
        return L

    L.sort()
    recur(L)
    return best[1]


import math
import random
def minimum_distance_naive(points):
    min_d = math.inf
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i + 1, len(points)):
            p2 = points[j]
            min_d = min(distance(p1, p2), min_d)
    return min_d


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# print(minimum_distance_incorrect(points))
print(minimum_distance(points))
# n = 4
# points = [(3, 5), (5, 10), (2, 5), (-10, 7)]
# points = [(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]

# print(minimum_distance_naive(points))


# n = 3
# points = [(-9, 1), (-8, 10), (9, 5)]
# print(minimum_distance(points))

# def stress_testing():
#     while True:
#         n = random.randint(1, 3)
#         points = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]
#         if minimum_distance_naive(points) != minimum_distance(points):
#             print('Failed')
#             print(n)
#             print(points)
#             break
#
# stress_testing()