import sys
sys.setrecursionlimit(500000)


class Graph:
    def __init__(self, a, edges):
        self.a = a
        self.edge = list(list() for i in range(len(a)))
        for i in edges:
            self.edge[i[0]].append(i[1])
            self.edge[i[1]].append(i[0])
        self.visited = [False for i in range(len(a))]
        self.order = list()

    def dfs(self, v):
        if self.visited[v]:
            return
        self.visited[v] = True
        for i in self.edge[v]:
            if not self.visited[i]:
                self.order.append((v, i))
                self.dfs(i)


def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    graph = Graph(a, edges)
    for i in range(len(a)):
        graph.dfs(i)
    for i in reversed(graph.order):
        a[i[0]] += a[i[1]]
        answer += abs(a[i[1]])
    return answer


_a = [-5, 0, 2, 1, 2]
_edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
# _a = [4, -4]
# _edges = [[0, 1]]
# result = 9
print(solution(_a, _edges))
