import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, key, position):
        self.key = key
        self.position = position
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.pre = list()
        self.post = list()

    def insert(self, node):
        index, level = 0, 0
        for i, j in enumerate(node):
            if level < j.position[1]:
                index = i
                level = j.position[1]
        self.pre.append(node[index].key) if node else None
        if 0 <= index < len(node):
            node[index].left = self.insert(node[:index])
            node[index].right = self.insert(node[index + 1:])
        self.post.append(node[index].key) if node else None
        return node[index] if node else None


def solution(nodeinfo):
    node = list(sorted([Node(i + 1, j) for i, j in enumerate(nodeinfo)], key=lambda x: x.position))
    tree = Tree()
    tree.insert(node)
    return [tree.pre, tree.post]


ni = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(ni))
