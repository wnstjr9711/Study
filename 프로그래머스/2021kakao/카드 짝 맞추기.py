from itertools import permutations
from collections import defaultdict


def getMove(points):
    count = 0
    for i in range(len(points) - 1):
        piv1 = (points[i][0], points[i + 1][1])  # 좌우 선 이동 시 중간점
        piv2 = (points[i + 1][0], points[i][1])  # 상하 선 이동 시 중간점
        route1 = [[(points[i][0], r) for r in (range(points[i][1] + 1, piv1[1] + 1) if piv1[1] > points[i][1] else range(points[i][1] - 1, piv1[1] - 1, -1))],
                  [(r, points[i + 1][1]) for r in (range(piv1[0] + 1, points[i + 1][0] + 1) if points[i + 1][0] > piv1[0] else range(piv1[0] - 1, points[i + 1][0] - 1, -1))]]
        route2 = [[(r, points[i][1]) for r in (range(points[i][0] + 1, piv2[0] + 1) if piv2[0] > points[i][0] else range(points[i][0] - 1, piv2[0] - 1, -1))],
                  [(points[i + 1][0], r) for r in (range(piv2[1] + 1, points[i + 1][1] + 1) if points[i + 1][1] > piv2[1] else range(piv2[1] - 1, points[i + 1][1] - 1, -1))]]
        r1sum1 = len(route1[0]) if sum(map(lambda x: x in points[i + 1:] or x[1] in (0, 3), route1[0])) == 0 else sum(map(lambda x: x in points[i + 1:] or x[1] in (0, 3), route1[0]))
        r1sum2 = len(route1[1]) if sum(map(lambda x: x in points[i + 1:] or x[0] in (0, 3), route1[1])) == 0 else sum(map(lambda x: x in points[i + 1:] or x[0] in (0, 3), route1[1]))
        r2sum1 = len(route2[0]) if sum(map(lambda x: x in points[i + 1:] or x[0] in (0, 3), route2[0])) == 0 else sum(map(lambda x: x in points[i + 1:] or x[0] in (0, 3), route2[0]))
        r2sum2 = len(route2[1]) if sum(map(lambda x: x in points[i + 1:] or x[1] in (0, 3), route2[1])) == 0 else sum(map(lambda x: x in points[i + 1:] or x[1] in (0, 3), route2[1]))
        count += min(r1sum1 + r1sum2, r2sum1 + r2sum2)
    return count


def getPoint(order, move, total):  # 이동 좌표 나열
    if not order:
        total.append(move)
        return
    cur = order[0]
    getPoint(order[1:], move + [cur[0], cur[1]], total)
    getPoint(order[1:], move + [cur[1], cur[0]], total)


def solution(board, r, c):
    answer = list()
    cards = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board)):
            cards[board[i][j]].append((i, j)) if board[i][j] != 0 else None
    orders = list(permutations(cards, len(cards)))
    for order in orders:
        total, count = list(), list()
        getPoint(list(map(lambda x: cards[x], order)), [(r, c)], total)
        for t in total:
            count.append(getMove(t))
        answer.append(min(count))
    return min(answer) + 2 * len(cards)


_b = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
_r = 1
_c = 0
# _b = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
# _r = 0
# _c = 1
print(solution(_b, _r, _c))
