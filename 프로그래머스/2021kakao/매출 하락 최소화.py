def dfs(tree, visited, emp, order):
    order.append(emp)
    visited[emp] = True
    for i in tree[emp]:
        if not visited[i]:
            dfs(tree, visited, i, order)


def solution(sales, links):
    inf = pow(2, 31)
    sales = [0] + sales
    dp1, dp2 = dict(), dict()
    tree = [list() for i in range(len(sales))]
    visited = [True] + [False for i in range(len(tree) - 1)]
    order = list()

    for i in links:
        tree[i[0]].append(i[1])

    for i in range(len(visited)):
        if not visited[i]:
            dfs(tree, visited, i, order)

    for i in reversed(order):
        if not tree[i]:
            dp1[i], dp2[i] = 0, sales[i]
        else:
            participate = False
            dp1[i] = sum(map(lambda x: min(dp1[x], dp2[x]), tree[i]))
            for j in tree[i]:
                if dp2[j] <= dp1[j]:
                    participate = True
            min_sum = inf
            if not participate:
                for j in tree[i]:
                    min_sum = min(min_sum, dp2[j] - dp1[j])
                dp1[i] += min_sum
            dp2[i] = sum(map(lambda x: min(dp1[x], dp2[x]), tree[i])) + sales[i]

    return min(dp1[1], dp2[1])


# _sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
# _links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# _sales = [5, 6, 5, 3, 4]
# _links = [[2, 3], [1, 4], [2, 5], [1, 2]]
# _sales = [5, 6, 5, 1, 4]
# _links = [[2, 3], [1, 4], [2, 5], [1, 2]]
_sales = [10, 10, 1, 1]
_links = [[3, 2], [4, 3], [1, 4]]


print(solution(_sales, _links))
