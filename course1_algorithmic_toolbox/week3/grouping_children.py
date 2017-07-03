"""
Many children came to a celebration.
Organize them into the minimum possible number of groups
such that the age of any two children in the same group
differ by at most one year.

Naive solution is:
to construct all possible subset combinations and loop through
them and invalidate the subsets which violate the 1 year condition.
then find the minimum length of these subsets and use that.

Complexity is 2^n
"""



def greedy_strategy(children, min_gap):
    """ O(n)
    sorted list of age of children
    :param children:
    :return:
    """
    groups = []
    previous = -1
    group = []
    for c in children:
        if group and c - min(group) > min_gap:
            # end the group
            groups.append(group)
            group = []
        group.append(c)
    groups.append(group)
    return groups

print(greedy_strategy([3.2, 3.8, 4.6, 5], 1))