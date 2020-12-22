class Two_Way_Chaining:
    class Node:
        def __init__(self, key, data, link):
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size):
        self.M = size
        self.a = [None] * size

    def hash(self, key):
        return key % self.M

    def d_hash(self, key):
        return self.hash(key) // 2 + 1

    def length(self,a):
        count = 0
        while a != None:
            count += 1
            a = a.next
        return count
    
    def put(self, key, data):
        i = self.hash(key)
        j = self.d_hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                p.data = data
                return
            p = p.next
        if self.a[i] != None:
            if self.a[j] != None:
                if self.length(self.a[i]) > self.length(self.a[j]):
                    self.a[j] = self.Node(key,data,self.a[j])
                else:
                    self.a[i] = self.Node(key, data, self.a[i])
            else:
                self.a[j] = self.Node(key, data, self.a[j])
        else:
            self.a[i] = self.Node(key, data, self.a[i])

    def get(self, key):
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next
        return None

    def print_table(self):
        for i in range(self.M):
            print('%2d' % (i), end='')
            p = self.a[i]
            while p != None:
                print('->[', p.key, ',', p.data, ']', end='')
                p = p.next
            print()


t = Two_Way_Chaining(13)
t.put(25, 'grape')
t.put(37, 'apple')
t.put(18, 'banana')
t.put(55, 'cherry')
t.put(22, 'mango')
t.put(35, 'lime')
t.put(50, 'orange')
t.put(63, 'watermelon')
print('탐색 결과:')
print('50의 data =', t.get(50))
print('63의 data =', t.get(63))
print('해쉬테이블:')
t.print_table()
