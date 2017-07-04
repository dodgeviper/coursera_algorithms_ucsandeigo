# Uses python3
"""Edit distance"""
# import numpy as np
# def EditDistance(str1, str2):
#     a = np.zeros((len(str1), len(str2)), dtype=np.int16)
#     for i in range(len(str1)):
#         a[i][0] = i
#
#     for j in range(len(str2)):
#         a[0][j] = j
#
#     for i in range(1, len(str1)):
#         for j in range(1, len(str2)):
#             insertion = a[i][j - 1] + 1
#             deletion = a[i - 1][j] + 1
#             match = a[i - 1][j - 1]
#             mismatch = a[i - 1][j - 1] + 1
#             if str1[i] == str2[j]:
#                 a[i][j] = min(insertion, deletion, match)
#             else:
#                 a[i][j] = min(insertion, deletion, mismatch)
#
#     return a[len(str1) - 1][len(str2) -1]


# Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


s1 = input()
s2 = input()
print(levenshtein(s1, s2))