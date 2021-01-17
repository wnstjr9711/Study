def solution(str1, str2):
    set1, set2 = list(), list()
    for i in range(max(len(str1), len(str2))):
        set1.append(str1[i:i+2].upper()) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2 else None
        set2.append(str2[i:i+2].upper()) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2 else None
    intersect, union = list(), list()
    for i in set(set1).union(set(set2)):
        union.append(max(set1.count(i), set2.count(i)))
    for i in set(set1).intersection(set(set2)):
        intersect.append(min(set1.count(i), set2.count(i)))
    return int((sum(intersect) / sum(union) if sum(union) != 0 else 1) * 65536)


s1 = 'FRANCE'
s2 = 'french'
# s1 = 'handshake'
# s2 = 'shake hands'
# s1 = 'aa1+aa2'
# s2 = 'AAAA12'
# s1 = 'E=M*C^2'
# s2 = 'e=m*c^2'

print(solution(s1, s2))