def solution(p):
    p = list(map(''.join, reversed(divide(p) + [['']])))
    for i, j in enumerate(p):
        if j.startswith(')'):
            p[i] = '(' + p[i - 1] + ')' + ''.join(map(lambda x: ')' if x == '(' else '(', list(j[1:-1])))
        elif j.startswith('('):
            p[i] = p[i] + p[i - 1]
        else:
            continue
        p[i-1] = ''
    return ''.join(reversed(p))


def divide(p):
    t = list()
    s = list()
    for i in p:
        if t.count('(') != t.count(')') or not t:
            t.append(i)
            if t.count('(') == t.count(')'):
                s.append(t)
                t = list()
    return s


print(solution(('(()())()')))
