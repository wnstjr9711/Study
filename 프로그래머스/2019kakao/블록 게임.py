def solution(board):
    blocks = dict()
    square = dict()
    depend = dict()
    enable = dict()
    for i in board:
        print(i)
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] != 0:
                if board[x][y] not in blocks:
                    blocks[board[x][y]] = {(x, y)}
                else:
                    blocks[board[x][y]].add((x, y))
    for k, v in blocks.items():
        temp = list(map(lambda p: p[0], list(sorted(v))))
        count = list(map(lambda p: temp.count(p), temp))
        if count != list(sorted(count)):
            enable[k] = False
        else:
            enable[k] = True
        for i in map(lambda p: p[0], v):  # 채워질 부분
            for j in map(lambda p: p[1], v):
                if k not in square:
                    square[k] = {(i, j)}
                else:
                    square[k].add((i, j))
        square[k].difference_update(v)
        for i, j in square[k]:  # 의존하는 블록
            for key in map(lambda b: b[j], board[:i + 1]):
                if key != 0 and key != k:
                    if k not in depend:
                        depend[k] = [key]
                    else:
                        depend[k].append(key) if key not in depend[k] else None
    for k, d in depend.items():
        dependEnable(k, d, depend, enable)
    return sum(enable.values())


def dependEnable(k, d, depend, enable):
    if not enable[k]:
        return False
    for dk in d:
        if (dk not in depend and not enable[dk]) or (dk in depend and not dependEnable(dk, depend[dk], depend, enable)):
            enable[k] = False
            return False
    return True








# bb = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
# bb = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
# bb = [[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]
bb = [[0,0,2,0,0],[0,1,2,4,4],[3,1,2,2,4],[3,1,1,0,4],[3,3,0,0,0]]

# bb= [[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
print(solution(bb))

