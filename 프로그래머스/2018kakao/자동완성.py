class Node:
    def __init__(self, key):
        self.key = key
        self.children = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node(w)
            cur.children[w].count += 1
            cur = cur.children[w]

    def search(self, word):
        count = 0
        cur = self.head
        for w in word:
            count += 1
            cur = cur.children[w]
            if cur.count == 1:
                return count
        return count


def solution(words):
    answer = 0
    trie = Trie()
    for w in words:
        trie.insert(w)
    for w in words:
        answer += trie.search(w)
    return answer


_word = ['go', 'gone', 'guild']
# _word = ['abc', 'def', 'ghi', 'jklm']
# _word = ['word', 'war', 'warrior', 'world']

print(solution(_word))
