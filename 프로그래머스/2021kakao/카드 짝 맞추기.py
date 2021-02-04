from collections import defaultdict
from itertools import permutations


def getMove(point1, point2): return sum(map(lambda x: 0 if x[1] - x[0] == 0 else 1, zip(point1, point2)))


def getCount(rc, order, c, count):
    if not order:
        count.append(c)
        return
    cur = order[0]
    getCount(cur[1], order[1:], c + getMove(rc, cur[0]), count)
    getCount(cur[0], order[1:], c + getMove(rc, cur[1]), count)


def solution(board, r, c):
    answer = 0
    pair = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board)):
            pair[board[i][j]].append((i, j)) if board[i][j] != 0 else None
    for p in pair.values():
        answer += getMove(p[0], p[1]) + 2
    total = list()
    order = tuple(permutations(pair, len(pair)))
    for o in order:
        check_position, count = (r, c), list()
        getCount(check_position, list(map(lambda x: pair[x], o)), 0, count)
        total.append(min(count))
    return answer + min(total)


_b = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
_r = 1
_c = 0
# _b = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
# _r = 0
# _c = 1
print(solution(_b, _r, _c))
