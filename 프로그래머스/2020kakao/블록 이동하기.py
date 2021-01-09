class Block:
    def __init__(self, board):
        self.board = board
        self.history = set()
        self.move_p = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.length = {(1, 1, 1): 0}

    def connect(self, x, y, h):
        self.history.add((x, y, h))
        c = list()
        if h == 0:  # 수직
            for i in self.move_p:
                if self.board[x + i[0]][y + i[1]] == self.board[x + i[0] + 1][y + i[1]] == 0 and (x + i[0], y + i[1], h) not in self.history:
                    self.history.add((x + i[0], y + i[1], h))
                    c.append((x + i[0], y + i[1], h))
            if self.board[x][y - 1] == self.board[x + 1][y - 1] == 0 and not self.history.issuperset({(x, y - 1, 1), (x + 1, y - 1, 1)}):  # 좌측 회전
                add = {(x, y - 1, 1), (x + 1, y - 1, 1)}.difference(self.history)
                self.history.update(add)
                c.extend(list(map(tuple, add)))
            if self.board[x][y + 1] == self.board[x + 1][y + 1] == 0 and not self.history.issuperset({(x, y + 1, 1), (x + 1, y + 1, 1)}):  # 우측 회전
                add = {(x, y, 1), (x + 1, y, 1)}.difference(self.history)
                self.history.update(add)
                c.extend(list(map(tuple, add)))
        else:  # 수평
            for i in self.move_p:
                if self.board[x + i[0]][y + i[1]] == self.board[x + i[0]][y + i[1] + 1] == 0 and (x + i[0], y + i[1], h) not in self.history:
                    self.history.add((x + i[0], y + i[1], h))
                    c.append((x + i[0], y + i[1], h))
            if self.board[x - 1][y] == self.board[x - 1][y + 1] == 0 and not self.history.issuperset({(x - 1, y, 0), (x - 1, y + 1, 0)}):  # 위로 회전
                add = {(x - 1, y, 0), (x - 1, y + 1, 0)}.difference(self.history)
                self.history.update(add)
                c.extend(list(map(tuple, add)))
            if self.board[x + 1][y] == self.board[x + 1][y + 1] == 0 and not self.history.issuperset({(x, y, 0), (x, y + 1, 0)}):  # 아래로 회전
                add = {(x, y, 0), (x, y + 1, 0)}.difference(self.history)
                self.history.update(add)
                c.extend(list(map(tuple, add)))
        for i in c:
            self.length[i] = self.length[(x, y, h)] + 1
        return c

    def bfs(self, x, y, h):
        que = list()
        for i in self.connect(x, y, h):
            que.append(i)
        while que:
            after = que.pop(0)
            if after in ((len(self.board) - 2, len(self.board) - 3, 1), (len(self.board) - 3, len(self.board) - 2, 0)):
                return self.length[(after[0], after[1], after[2])]
            for i in self.connect(after[0], after[1], after[2]):
                que.append(i)


def solution(board):
    board_pad = [[1 for i in range(len(board) + 2)] for j in range(len(board) + 2)]
    for i in range(len(board)):
        board_pad[i + 1][1:-1] = board[i]
    block = Block(board_pad)
    return block.bfs(1, 1, 1)


b = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
print(solution(b))
