def solution(record):
    user = dict()
    result = list()
    msg = list(map(lambda x: x.split(), record))
    for m in msg:
        if len(m) == 3:
            user[m[1]] = m[2]
    for p in msg:
        if p[0] == 'Enter':
            result.append("{}님이 들어왔습니다.".format(user[p[1]]))
        elif p[0] == 'Leave':
            result.append("{}님이 나갔습니다.".format(user[p[1]]))
    return result


r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))