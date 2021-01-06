class Node:
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        this = self.head
        for char in word:
            if char not in this.children:
                this.children[char] = Node(char)
            this.children[char].count += 1
            this = this.children[char]

    def search(self, word):
        this = self.head
        for char in word:
            if char not in this.children:
                return sum(map(lambda x: x.count, this.children.values())) if char == '?' else 0
            this = this.children[char]


def solution(words, queries):
    trie = dict()
    r_trie = dict()
    for word in words:
        if str(len(word)) in trie:
            trie[str(len(word))].insert(word)
            r_trie[str(len(word))].insert(word[::-1])
        else:
            trie[str(len(word))] = Trie()
            trie[str(len(word))].insert(word)
            r_trie[str(len(word))] = Trie()
            r_trie[str(len(word))].insert(word[::-1])
    answer = list()
    for q in queries:
        if q.endswith('?'):
            answer.append(trie[str(len(q))].search(q) if str(len(q)) in trie else 0)
        else:
            answer.append(r_trie[str(len(q))].search(q[::-1]) if str(len(q)) in r_trie else 0)
    return answer


_words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
_queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(_words, _queries))
