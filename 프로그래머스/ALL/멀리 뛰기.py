from math import comb
import math


def solution(n):
    answer = 0
    for i in reversed(range(math.ceil(n / 2), n + 1)):
        answer += comb(i, n - i)
    return answer % 1234567
