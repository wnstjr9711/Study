def solution(cacheSize, cities):
    answer = 0
    print(cacheSize, cities)
    return answer


cs = 3
ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
# cs = 3
# ct =['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
# cs = 2
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
# cs = 5
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
# cs = 2
# ct = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
# cs = 0
# ct = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution(cs, ct))