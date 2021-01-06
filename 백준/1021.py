N, M = list(map(int, input().split()))      # N = 10, M = 3
index = list(map(int, input().split()))     # index = [2, 9, 5]
queue = list(range(1, N+1))

count = 0
start = 1
for i in range(M):
    count += min(abs(queue.index(index[i])-queue.index(start)), N - abs(queue.index(index[i])-queue.index(start)))
    if queue.index(index[i]) == N-1:
        start = queue[0]
    else:
        start = queue[queue.index(index[i])+1]
    queue.remove(index[i])
    N -= 1

print(count)