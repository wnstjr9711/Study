from collections import defaultdict


def solution(a):
    counts = defaultdict(int)
    stack = {i: None for i in a}
    for i in range(len(a)):
        for s in stack:
            if stack[s] is not None and stack[s] != a[i]:
                if stack[s] == s:
                    stack[s] = None
                    counts[s] += 1
                elif a[i] == s:
                    stack[s] = None
                    counts[a[i]] += 1
            else:
                stack[s] = a[i]
    return (max([0] + list(counts.values()))) * 2

# _a = [0]
_a = [5, 2, 3, 3, 5, 3]
# _a = [0, 3, 3, 0, 7, 2, 0, 2, 2, 0]
print(solution(_a))
