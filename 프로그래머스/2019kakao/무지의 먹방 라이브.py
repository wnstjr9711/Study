class Node:
    def __init__(self, number, time):
        self.number = number
        self.time = time
        self.left, self.right = None, None


class CList:
    def __init__(self, s, n):
        self.size = s
        self.nodes = n
        self.point = n[0]

    def delete(self, k):
        loop, left = k // self.size, k % self.size   # 2
        for i, j in enumerate(self.nodes):
            if loop < j.time:
                j.time -= loop
            elif j.time != 0:
                self.size -= 1
                j.left.right, j.right.left = j.right, j.left
                if j == self.point:
                    self.point = j.right if j.right != j else None
                left += loop - j.time
                j.time = 0
        if left >= self.size != 0:
            return self.delete(left)
        return left

    def count(self, k):
        if self.point:
            for i in range(k):
                self.point = self.point.right
            return self.point.number
        else:
            return -1


def solution(food_times, k):
    nodes = [Node(i + 1, j) for i, j in enumerate(food_times)]
    for i, j in enumerate(nodes):
        j.left = nodes[i - 1]
        j.right = nodes[i + 1] if i < len(nodes) - 1 else nodes[0]
    c = CList(len(nodes), nodes)
    return c.count(c.delete(k))


ft = [3, 1, 2]
kk = 4
print(solution(ft, kk))
