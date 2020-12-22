class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height

    def balance(self, n):
        if self.df(n) > 1:
            if self.df(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
        elif self.df(n) < -1:
            if self.df(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n  ## 반환값 꼭 지정!!

    def df(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return x

    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value  # key가 이미 트리에 있으므로 value 갱신
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)  # 노드 n의 균형 점검 및 불균형을 바로 잡음

    def preorder(self, n):  # 전위순회
        print(str(n.key), ' ', end='')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)

    def inorder(self, n):  # 중위순회
        if n.left:
            self.inorder(n.left)
        print(str(n.key), ' ', end='')
        if n.right:
            self.inorder(n.right)

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def del_min(self):
        if self.root == None:
            return None
        self.root = self.del_minimum(self.root)

    def del_minimum(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_minimum(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete(self, key):
        if self.root == None:
            return None
        self.root = self.delete_node(self.root, key)

    def delete_node(self, n, key):
        if n.key > key:
            n.left = self.delete_node(n.left, key)
        elif n.key < key:
            n.right = self.delete_node(n.right, key)
        else:
            if n.left == None:
                return n.right
            elif n.rigth == None:
                return n.left
            target = n
            n = self.minimum(target.right)
            n.left = target.left
            n.right = self.del_minimum(target.right)
        n.heigt = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)


t = AVL()
t.put(75, 'apple')
t.put(80, 'grape')
t.put(85, 'lime')
t.put(20, 'mango')
t.put(10, 'strawberry')
t.put(50, 'banana')
t.put(30, 'cherry')
t.put(40, 'watermelon')
t.put(70, 'melon')
t.put(90, 'plum')
t.inorder(t.root)
t.del_min()
print('\n')
t.inorder(t.root)
t.delete(50)
print('\n')
t.inorder(t.root)
