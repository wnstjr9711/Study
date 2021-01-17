def solution(m, n, board):
    board = [list(reversed([x[i] for x in board])) for i in range(n)]
    return get2x2(n, m, board)


def get2x2(n, m, board):
    removed = 0
    positions = set()
    for i in range(n - 1):
        for j in range(m - 1):
            check = list(map(lambda x: x[j: j + 2], board[i: i + 2]))
            if check[0][0] == check[0][1] is not None and check[0] == check[1]:
                positions.update({(i, j), (i + 1, j + 1), (i + 1, j), (i, j + 1)})
    for p in positions:
        board[p[0]][p[1]] = None
        removed += 1
    for i in board:
        for j in i:
            if j is None:
                i.remove(j) or i.append(None)
    if removed != 0:
        removed += get2x2(n, m, board)
    return removed



# mm = 4
# nn = 5
# bd = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']

mm = 6
nn = 6
bd = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

print(solution(mm, nn, bd))
