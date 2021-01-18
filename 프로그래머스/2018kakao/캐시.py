def solution(cacheSize, cities):
    cache = list()
    answer = 0
    for c in list(map(lambda x: x.upper(), cities)):
        if c not in cache:
            answer += 5
            cache.append(c)
            cache.pop(0) if len(cache) > cacheSize else None
        else:
            answer += 1
            cache.remove(c)
            cache.append(c)
    return answer


# cs = 3
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
# cs = 3
# ct =['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
# cs = 2
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
# cs = 5
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cs = 2
ct = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
# cs = 0
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution(cs, ct))