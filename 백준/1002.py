import math

T = int(input())
ans = list()

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    if distance > r1 + r2:
        ans.append(0)
    elif distance < r1 + r2:
        if distance == 0 and r1 == r2:
            ans.append(-1)
        elif distance + min(r1, r2) == max(r1, r2):
            ans.append(1)
        elif distance + min(r1, r2) < max(r1, r2):
            ans.append(0)
        else:
            ans.append(2)
    else:
        ans.append(1)

while ans:
    print(ans.pop(0))