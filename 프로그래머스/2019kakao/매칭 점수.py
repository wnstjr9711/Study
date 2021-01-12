# 기본점수: 검색어 개수
# 외부 링크 수: 하이퍼링크 수
class Url:
    def __init__(self, html):
        self.data = html
        self.key = None
        self.word = 0
        self.link = 0

    def makeKey(self):
        self.data = self.data.split('</head>')
        for meta in self.data[0].split('<'):
            for url in meta.split('"') if meta.startswith('meta') else []:
                if url.startswith('https://'):
                    self.key = url
        return self.key

    def wordcount(self, word):
        check = self.data[1]
        for i in check:
            check = check.replace(i, ' ') if not i.isalpha() else check
        check = check.split()
        check = list(map(lambda x: x.lower(), check))
        self.word = check.count(word)

    def addLink(self, keys):
        outer = list(map(lambda x: eval(x.split('>')[0]) if x.startswith('"https') else None, self.data[1].split('<a href=')))
        while None in outer:
            outer.remove(None)
        for o in outer:
            if o in keys.keys():
                keys[o].link += self.word / len(outer)


def solution(word, pages):
    url = dict()
    for page in pages:
        u = Url(page)
        url[u.makeKey()] = u
        u.wordcount(word.lower())

    for u in url.values():
        u.addLink(url)

    answer = list()
    for u in url.values():
        answer.append((u.word + u.link))

    return answer.index(max(answer))


w = 'blind'
p = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# w = 'Muzi'
# p = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(w, p))