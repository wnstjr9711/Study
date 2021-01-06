class Slist:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1;

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
        self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            t = p.next
            p.next = t.next
            self.size -= 1

    def search(self, target):
        p = self.head
        for i in range(self.size):
            if target == p.item:
                return i
            p = p.next
        return None

    def print_list(self):
        p = self.head
        for i in range(self.size):
            print(p.item, '->', end='')
            p = p.next
        print('\n')


class EmptyError(Exception):
    pass


s = Slist()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry', s.head.next)
s.insert_front('pear')
s.print_list()
print('cherry %d번째' % s.search('cherry'))
print('kiwi는', s.search('kiwi'))
print('배 다음 노드 삭제 후: \n', end='')
s.delete_after(s.head)
s.print_list()
print('첫 노드 삭제 후:\n', end='')
s.delete_front()
s.print_list()
print('첫 노드로 망고, 딸기 삽입 후:\n', end='')
s.insert_front('mango')
s.insert_front('strewberry')
s.print_list()
s.delete_after(s.head.next.next)
print('오렌지 다음 노드 삭제 후:\n')
s.print_list()
