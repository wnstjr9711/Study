import math


def solution(n, stations, w):
    answer = 0
    left = list()
    i = 1
    for s in stations:
        left.append(s - w - i)
        i = s + w + 1
    left.append(n - i + 1)
    for l in left:
        answer += math.ceil(l / (2 * w + 1))
    return answer
