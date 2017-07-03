# Uses python3
"""Organizing lottery
You are orgnaizing an online lottery. To participate a person bets on a single
integer. You then draw several ranges of consecutive integers at random. A participants
payoff is then proportional to the number of ranges that contain the participants
number minus the number of ranges that does not contain it. You need an efficient
algorithm for computing the payoffs for all participants. A naive way to do this is
simply scan for all participants, the list of ranges. However, you lottery is very
popular; you have thousands of participants and thousands of ranges. for this reason
you cannot afford to have a slow naive algorithm.

Task: You are given a set of points on a line and set of segments on a line. The
goal is to compute for each point, the number of segments that contain this point.

Input:
The first line contains the two non-negative integers s and p defining the number
of segments and the number fo points on a line, respectively. The next s lines contain
two integers ai, bi defining the ith segment [ai, bi]. The next line contains p integers
defining points x1, x2, ... xp.

Constraints:
1<= s, p <= 50000; -10^8 <= ai <= bi <= 10^8 for all 0 <= i < s;

Output format:
Output p non-negative integers k0, k1,...kp-1 where ki is the number of segments
which contain xi. More formally:
ki = |{j: aj <= xi <= bj }|
"""




def naive_solution(ranges, participant_numbers):
    scores = {}
    for x in participant_numbers:
        if scores.get(x, None) is not None:
            continue
        for y in ranges:
            yi, yj = y
            if yi <= x <= yj:
                scores[x] = scores.get(x, 0) + 1
    return [scores.get(x, 0) for x in participant_numbers]



### Efficient solution

BEGIN, POINT, END = range(3)

import collections

def winning_proportions(ranges, participants):
    # sort on the starting point O(nlogn)
    point_pairs = []
    for start, end in ranges:
        point_pairs.append((start, BEGIN))
        point_pairs.append((end, END))

    point_map = collections.defaultdict(set)
    for i in range(len(participants)):
        point_pairs.append((participants[i], POINT))
        point_map[participants[i]].add(i)

    sorted_points = sorted(point_pairs, key=lambda p: (p[0], p[1]))

    count = [0] * len(participants)
    coverage = 0
    for pair in sorted_points:
        if pair[1] == BEGIN:
            coverage += 1
        if pair[1] == END:
            coverage -= 1
        if pair[1] == POINT:
            indices = point_map[pair[0]]
            # to handle non-unique points
            for i in indices:
                count[i] = coverage

    return count


segments, participants = tuple(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(segments)]
participants = list(map(int, input().split()))
# print(naive_solution(ranges, participants))
print(' '.join(map(str, winning_proportions(ranges, participants))))

import random


def stress_testing():
    while True:
        segments = random.randint(1, 5)
        participants = random.randint(1, 5)
        ranges = []
        for _ in range(segments):
            start = random.randint(-10, 10)
            end = random.randint(start , 10)
            ranges.append((start, end))
        participant_numbers = [random.randint(-10, 10) for _ in range(participants)]
        if naive_solution(ranges, participant_numbers) != winning_proportions(ranges, participant_numbers):
            print('Failed:')
            print(segments, participants)
            print(ranges)
            print(participant_numbers)
            break

# stress_testing()
#
# ranges = [(-9, 4), (4, 9)]
# participants = [-2, -3, 4, 4]
# # print(participants)
# print(naive_solution(ranges, participants))
# print(winning_proportions(ranges, participants))