import sys
sys.setrecursionlimit(300000)


class Tree:
    def __init__(self, n, edges):
        self.adjacent = [list() for i in range(n + 1)]
        for i in edges:
            self.adjacent[i[0]].append(i[1])
            self.adjacent[i[1]].append(i[0])
        self.visited = list()
        self.longest = list()
        self.start = 1

    def dfs(self, v, path):
        self.visited[v] = True
        for i in self.adjacent[v]:
            if not self.visited[i]:
                self.dfs(i, path + 1)
        self.longest.append([path, v])


def solution(n, edges):
    tree = Tree(n, edges)
    for i in range(3):
        tree.visited = [False for _ in range(n + 1)]
        tree.dfs(tree.start, 0)
        tree.longest.sort(key=lambda x: x[0], reverse=True)
        tree.start = tree.longest[0][1]
        if i == 2:
            return tree.longest[1][0]
        else:
            tree.longest.clear()


# nn = 3
# _edges = [[1, 2],[2, 3]]
# nn = 4
# _edges = [[1, 2], [2, 3], [3, 4]]
nn = 5
_edges = [[1, 5], [2, 5], [3, 5], [4, 5]]
print(solution(nn, _edges))
