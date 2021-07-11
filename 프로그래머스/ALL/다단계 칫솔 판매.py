def distribute(multilevel, this, amount, answer):
    if this in answer:
        d_amount = int(amount / 10)
        answer[this] += amount - d_amount
        if d_amount >= 1:
            distribute(multilevel, multilevel[this], d_amount, answer)
        else:
            answer[this] += d_amount


def solution(enroll, referral, seller, amount):
    multilevel = {enroll[i]: referral[i] for i in range(len(enroll))}
    answer = {i: 0 for i in enroll}
    for i in range(len(seller)):
        distribute(multilevel, seller[i], amount[i] * 100, answer)

    return list(answer.values())


_e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
_r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
_s = ["young", "john", "tod", "emily", "mary"]
_a = [12, 4, 2, 5, 10]

# _e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# _r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# _s = ["sam", "emily", "jaimie", "edward"]
# _a = [2, 3, 5, 4]

# result = [360, 958, 108, 0, 450, 18, 180, 1080]
# result = [0, 110, 378, 180, 270, 450, 0, 0]
print(solution(_e, _r, _s, _a))
