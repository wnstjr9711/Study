def solution(s):
    answer = list()
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        sl = 0
        word = list()
        while sl <= len(s):
            word.append(s[sl:sl + i])
            sl += i
        index = 0
        length = len(word[-1])
        for j, k in enumerate(word):
            if k == word[index]:
                continue
            else:
                count = j - index
                length += len(str(count)) + i if count != 1 else i
                index = j
        answer.append(length)
    return min(answer)