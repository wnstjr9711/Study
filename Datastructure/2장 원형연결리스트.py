class Clist:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_item(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):
        if self.is_empty():
            print("Not found")
        else:
            f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            print("Not found")
        else:
            x = self.last.next
            if self.size == 1:
                self.last = None
            else:
                self.last.next = x.next
            self.size -= 1

    def print(self):
        if self.is_empty():
            print("No found")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, '->', end='')
                p = p.next
            print(p.item)


c = Clist()
c.insert('pear')
c.insert('cherry')
c.insert('orange')
c.insert('apple')
c.print()
print('c의 길이:', c.no_item())
print('c의 첫항목: ', c.first())
c.delete()
print('첫 노드 삭제 후: ', end='')
c.print()
print('c의 길이:', c.no_item())
print('c의 첫항목: ', c.first())
c.delete()
print('첫 노드 삭제 후: ', end='')
c.print()
print('c의 길이:', c.no_item())
print('c의 첫항목: ', c.first())
c.delete()
print('첫 노드 삭제 후: ', end='')
c.print()
