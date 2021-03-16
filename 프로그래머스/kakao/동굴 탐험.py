class Tree:
    def __init__(self, n, path, order):
        self.path = [list() for i in range(n)]
        for i in path:
            self.path[i[0]].append(i[1])
            self.path[i[1]].append(i[0])
        self.visited = [False for i in range(n)]
        self.route = [None for i in range(n)]
        self.pre = dict()
        self.next = [0]
        for i in order:
            self.pre[i[1]] = i[0]

    def dfs(self, v):
        if v in self.pre:
            if not self.visited[self.pre[v]]:
                self.next.append(v)
                return
        self.visited[v] = True
        for i in self.path[v]:
            if not self.visited[i]:
                self.dfs(i)


def solution(n, path, order):
    tree = Tree(n, path, order)
    cycle = 0
    c = 0
    while tree.next:
        tree.dfs(tree.next.pop(0))
        print(tree.next)
        if cycle == len(tree.next):
            c += 1
            if c == cycle:
                return False
        else:
            cycle = len(tree.next)
            c = 0
    return True

_n = 9
_path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
_order = [[8,5],[6,7],[4,1]]
# _n = 9
# _path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
# _order = [[4,1],[5,2]]
# _n = 9
# _path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
# _order = [[4,1],[8,7],[6,5]]

print(solution(_n, _path, _order))
