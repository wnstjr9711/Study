import ast


def solution(s):
    s = ast.literal_eval(s.replace('{', '[').replace('}', ']'))
    s.sort(key=lambda x: len(x))
    s = list(map(lambda x: set(x), s))
    answer = list()
    temp = set()
    for i in s:
        answer.append(i.difference(temp).pop())
        temp = i
    return answer


_s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# _s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# _s = "{{20,111},{111}}"
# _s = "{{123}}"
# _s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(_s))
