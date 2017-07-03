"""Edit distance"""
import numpy as np
def EditDistance(str1, str2):
    a = np.zeros((len(str1), len(str2)), dtype=np.int16)
    for i in range(len(str1)):
        a[i][0] = i

    for j in range(len(str2)):
        a[0][j] = j

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            insertion = a[i][j - 1] + 1
            deletion = a[i - 1][j] + 1
            match = a[i - 1][j - 1]
            mismatch = a[i - 1][j - 1] + 1
            if str1[i] == str2[j]:
                a[i][j] = min(insertion, deletion, match)
            else:
                a[i][j] = min(insertion, deletion, mismatch)

    return a[len(str1) - 1][len(str2) -1]


s1 = input()
s2 = input()
print(EditDistance(s1, s2))