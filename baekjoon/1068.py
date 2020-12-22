class Tree:
    class Node:
        def __init__(self, num):
            self.num = num
            self.children = list()

    def __init__(self):
        self.root = None


N = int(input())  # 노드 개수
parent = list(map(int, input().split()))
T = Tree()
node = []

for i in range(len(parent)):
    node.append(T.Node(i))

for j in range(len(parent)):
    if parent[j] == -1:
        T.root = node[j]
    else:
        node[parent[j]].children.append(node[j])

del_num = int(input())


def del_node(node_num):
    if node[node_num].children:
        for c in reversed(node[node_num].children):
            del_node(c.num)
    node[node_num].children = 'empty'


if node[del_num] in node[parent[del_num]].children:
    node[parent[del_num]].children.remove(node[del_num])
del_node(del_num)

count = 0
for n in node:
    if not n.children:
        count += 1
print(count)