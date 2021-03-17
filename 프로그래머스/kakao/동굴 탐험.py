class Tree:
    def __init__(self, n, path, order):
        self.path = [list() for i in range(n)]
        for i in path:
            self.path[i[0]].append(i[1])
            self.path[i[1]].append(i[0])
        self.visited = [False for i in range(n)]
        self.pre = {i[1]: i[0] for i in order}
        self.post = dict()

    def dfs(self, v):
        if v in self.pre and not self.visited[self.pre[v]]:
            self.post[self.pre[v]] = v
            return
        self.visited[v] = True
        if v in self.post:
            self.dfs(self.post[v])
        for i in self.path[v]:
            if not self.visited[i]:
                self.dfs(i)


def solution(n, path, order):
    tree = Tree(n, path, order)
    tree.dfs(0)
    if sum(tree.visited) == n:
        return True
    else:
        return False


# _n = 9
# _path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
# _order = [[8,5],[6,7],[4,1]]
# _n = 9
# _path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
# _order = [[4,1],[5,2]]
_n = 9
_path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
_order = [[4,1],[8,7],[6,5]]

print(solution(_n, _path, _order))
