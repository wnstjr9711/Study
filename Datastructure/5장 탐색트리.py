class Node:
    def __init__(self, key, item, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right


class Binary_Tree_Search:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, key):
        if n == None:
            return None
        if n.key > key:
            return self.get_item(n.left, key)
        elif n.key < key:
            return self.get_item(n.right, key)
        else:
            return n.key

    def put(self, key, item):
        self.root = self.put_item(self.root, key, item)

    def put_item(self, n, key, item):
        if n == None:
            return Node(key, item)
        elif n.key > key:
            n.left = self.put_item(n.left, key, item)
        elif n.key < key:
            n.right = self.put_item(n.right, key, item)
        else:
            n.item = item
        return n

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def preorder(self, n):
        print(n.key, ' ', end='')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)

    def levelorder(self):
        q = []
        q.append(self.root)
        while len(q) != 0:
            k = q.pop(0)
            print(k.key, ' ', end='')
            if k.left != None:
                q.append(k.left)
            if k.right != None:
                q.append(k.right)

    def del_min(self):
        if self.root == None:
            return None
        self.root = self.del_minimum(self.root)

    def del_minimum(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_minimum(n.left)
        return n

    def delete(self, k):
        if self.root == None:
            return None
        self.root = self.delete_node(self.root, k)

    def delete_node(self, n, k):
        if n.key > k:
            n.left = self.delete_node(n.left, k)
        elif n.key < k:
            n.right = self.delete_node(n.right, k)
        else:
            if n.left == None:
                return n.right
            elif n.right == None:
                return n.left
            target = n
            n = self.minimum(target.right)
            n.left = target.left
            n.right = self.del_minimum(target.right)
        return n


t = Binary_Tree_Search()
t.put(500, 'apple')
t.put(600, 'banana')
t.put(200, 'melon')
t.put(100, 'orange')
t.put(400, 'lime')
t.put(250, 'kiwi')
t.put(150, 'grape')
t.put(800, 'peach')
t.put(700, 'cherry')
t.put(50, 'pear')
t.put(350, 'lemon')
t.put(10, 'plum')
t.levelorder()
print('\n')
t.preorder(t.root)
print('\n')
print(t.get(600))
t.del_min()
t.preorder(t.root)
print('\n')
t.del_min()
t.levelorder()
print('\n')
t.delete(100)
t.levelorder()
