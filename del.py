import sys
people = []
A_n = []
a = 0

n = int(sys.stdin.readline())
for i in range(0,n):
    j = sys.stdin.readline().split()
    j = list(map(int, j))
    people.append(j)
    A_n.append(0)

for i in range(0,n):
    for j in range(0,n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            A_n[people.index(people[i])] += 1

for i in range(0,n):
    A_n[i]+=1

A_n = list(map(str, A_n))
print(' '.join(A_n))