def getTotal(cand, cover, temp):
    if cover:
        for i in cover[0]:
            getTotal(cand, cover[1:], temp + [i]) if i not in temp else None
    else:
        cand.add(tuple(sorted(temp)))


def solution(user_id, banned_id):
    answer = 0
    cover = [list() for i in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            match = True
            if len(banned_id[i]) == len(user_id[j]):
                for ii in range(len(banned_id[i])):
                    if not (banned_id[i][ii] == user_id[j][ii] or banned_id[i][ii] == '*'):
                        match = False
            else:
                match = False
            if match:
                cover[i].append(user_id[j])
    cand = set()
    getTotal(cand, cover, list())
    for i in cand:
        if len(i) == len(banned_id):
            answer += 1
    return answer





# uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# bid = ["fr*d*", "abc1**"]
uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
bid = ["*rodo", "*rodo", "******"]
# uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# bid = ["fr*d*", "*rodo", "******", "******"]

print(solution(uid, bid))
