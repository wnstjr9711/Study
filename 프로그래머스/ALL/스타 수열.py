from collections import defaultdict


def solution(a):
    counts = defaultdict(int)
    check = dict()
    for i in range(len(a)):
        if a[i] not in check:
            check[a[i]] = 0
        if i - check[a[i]] > 0 and a[check[a[i]]] != a[i]:
            counts[a[i]] += 1
            check[a[i]] = i + 1
        else:
            if i + 1 < len(a) and a[i + 1] != a[i]:
                counts[a[i]] += 1
                check[a[i]] = i + 2
    return (max([0] + list(counts.values()))) * 2


# _a = [0]
_a = [5, 2, 3, 3, 5, 3]
# _a = [0, 3, 3, 0, 7, 2, 0, 2, 2, 0]
_a = [1,1,1,1,1,1,2,3,2,4]
print(solution(_a))
