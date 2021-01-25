from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = list()
    for cour in course:
        count = defaultdict(int)
        for order in orders:
            for sets in list(combinations(list(sorted(order)), cour)):
                count[''.join(sets)] += 1
        for key, value in count.items():
            if value == max(count.values()) and value != 1:
                answer.append(key)
    return sorted(answer)


o = ["XYZ", "XWY", "WXA"]
c = [2, 3, 5]

print(solution(o, c))
