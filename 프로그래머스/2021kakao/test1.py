def solution(new_id):
    answer = list(new_id.lower())
    allow_char = ['-', '_', '.']
    answer = ''.join([i for i in answer if i.isalnum() or i in allow_char])
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer


n = "abcdefghijklmn.p"
print(solution(n))
