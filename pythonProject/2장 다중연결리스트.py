class Dlist:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1

    def print(self):
        if self.empty():
            print("Not found list")
        else:
            p = self.head.next
            for i in range(self.size):
                print(p.item, '<->', end='')
                p = p.next
            print('\n')


d = Dlist()
d.insert_after(d.head, 'apple')
d.insert_before(d.tail, 'orange')
d.insert_before(d.tail, 'cherry')
d.insert_after(d.head.next, 'pear')
d.print()
d.delete(d.head.next)
d.print()

