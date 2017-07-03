"""Edit distance"""
import numpy as np
def EditDistance(str1, str2):

    def OutputAlignment(i, j):
        # Backtracking
        if i == 0 and j == 0:
            return

        if i > 0 and a[i][j] == a[i - 1][j] + 1:
            OutputAlignment(i - 1, j)
            print(str1[i], '-')

        elif j > 0 and a[i][j] == a[i][j - 1] + 1:
            OutputAlignment(i, j - 1)
            print('-', str2[j])

        else:
            OutputAlignment(i - 1, j - 1)
            print(str1[i], str2[j])

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

    OutputAlignment(len(str1) - 1, len(str2) - 1)
    return a[len(str1) - 1][len(str2) -1]

print(EditDistance('editing', 'distance'))
print(EditDistance('axybc', 'abc'))

print(EditDistance('bread', 'really'))

print(EditDistance('kitten', 'sitting'))