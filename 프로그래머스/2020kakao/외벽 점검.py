from itertools import combinations


def available(l, d):
    dist = [i for i in d]
    for i in l:
        for j in dist:
            if i <= j:
                dist.remove(j)
                break
    if len(dist) + len(l) == len(d):
        return True
    else:
        return False


def solution(n, weak, dist):
    answer = -1
    for i in reversed(range(1, len(dist)+1)):
        for j in combinations(weak, i):
            length = list()
            w = weak[weak.index(j[0]):] + list(map(lambda x: x + n, weak[:weak.index(j[0])]))
            for k in reversed(j):
                length.append(w[w.index(k):][-1] - w[w.index(k):][0])
                w = w[:w.index(k)]
            if available(sorted(length, reverse=True), dist):
                answer = i
                break
    return answer


_n = 12
_weak = [1, 5, 6, 10]
# _weak = [1, 3, 4, 9, 10]
_dist = [1, 2, 3, 4]
# _dist = [3, 5, 7]

print(solution(_n, _weak, _dist))