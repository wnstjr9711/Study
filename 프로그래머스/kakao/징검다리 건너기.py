import bisect


def solution(stones, k):
    box = list(sorted(stones[:k]))
    answer = box[-1]

    for i in range(len(stones) - k):
        box.pop(bisect.bisect_left(box, stones[i]))
        bisect.insort_left(box, stones[i + k])
        if answer > box[-1]:
            answer = box[-1]
    return answer


_stone = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
_k = 3

print(solution(_stone, _k))
