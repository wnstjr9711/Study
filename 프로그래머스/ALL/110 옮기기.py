def solution(s):
    answer = []
    for i in s:
        stack = list()
        count = 0
        for ii in i:
            if ii == '0' and stack[-2:] == ['1', '1']:
                count += 1
                for _ in range(2):
                    stack.pop(-1)
            else:
                stack.append(ii)
        stack = ''.join(stack)
        put = '110' * count
        idx = stack.find('11')
        if idx != -1:
            stack = stack[:idx] + put + stack[idx:]
        else:
            zero = stack[::-1].find('0')
            if zero == -1:
                stack = put + stack
            else:
                zero = len(stack) - zero
                stack = stack[:zero] + put + stack[zero:]
        answer.append(stack)
    return answer


_s = ["1110", "0001110", "0111111010"]
# _s = ["1110", "100111100", "0111111010"]
# result = ["1101", "100110110", "0110110111"]
print(solution(_s))
# 110 > 000, 001, 010, 011, 100, 101
# 110