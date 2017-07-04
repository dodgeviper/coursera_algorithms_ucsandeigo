# Uses python3.
"""Longest common subsequence of three sequences

Goal: To compute the length of a longest common subsequence of three sequences.

Task:
Given three sequences. A = (a1, a2,.. an), B = (b1, b2... bm), C = (c1, c2.. cl) find the length
of their longest common subsequence i.e. the largest non-negative integer p such there exist
indices 1 <= i1 < i2 ...  < ip <= n, 1 <= j1 < j2.....<jp <= m, 1<= k1 < k2.... < kp <=l such that
ai1 = bj1 =ck1, .... aip = bjp = ckp

Input format: First line n. second line: a1, a2... an. Third line m, fourth line b1, b2.... bm and
fift line l, sixth line c1, c2.. cl

Constraints: 1<=n, m, l <= 100 and -10^9 < ai, bj, ck <= 10^9

Output: length of common subsequence
"""


#https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def LCS(s1, s2):
    table = [[''] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    print(table)
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            # String indexes are 1 off.
            if s2[i - 1] == s1[j - 1]:
                table[i][j] = table[i - 1][j - 1] + s1[j - 1]
            else:
                if len(table[i][j - 1]) > len(table[i - 1][j]):
                    table[i][j] = table[i][j - 1]
                else:
                    table[i][j] = table[i - 1][j]
    return table[-1][-1]


def LCS_3(s1, s2, s3):
    table = [[[''] * (len(s1) + 1)] * (len(s2) + 1) for _ in range(len(s3) + 1)]
    for i in range(len(s3)+ 1):
        for j in range(len(s2) + 1):
            for k in range(len(s1) + 1):
                if s1[k - 1] == s2[j - 1] == s3[i - 1]:
                    table[i][j][k] = table[i-1][j-1][k-1] + s1[k-1]
                else:
                    if len(table[i-1][j][k]) > len(table[i][j-1][k]) and len(table[i-1][j][k]) > len(table[i][j][k-1]):
                        table[i][j][k] = table[i-1][j][k]
                    elif len(table[i][j-1][k]) > len(table[i-1][j][k]) and len(table[i][j-1][k]) > len(table[i][j][k-1]):
                        table[i][j][k] = table[i][j-1][k]
                    else:
                        table[i][j][k] = table[i][j][k - 1]
    # print(table)
    return table[-1][-1][-1]


# s1 = 'BANANA'
# s2 = 'ATANA'

n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()
l = int(input())
s3 = input().split()

print(LCS(s1, s2))

print(LCS_3(s1, s2, s3))