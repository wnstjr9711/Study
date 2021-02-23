def dfs(tree, visited, emp, order):
    order.append(emp) if tree[emp] and emp != 1 else None
    # order.append(emp)
    visited[emp] = True
    for i in tree[emp]:
        if not visited[i]:
            dfs(tree, visited, i, order)


def solution(sales, links):
    sales = [None] + sales
    answer = dict()
    tree = [list() for i in range(len(sales))]
    team = [1 for i in range(len(sales))]
    visited = [True] + [False for i in range(len(tree) - 1)]
    order = list()

    for i in links:
        tree[i[0]].append(i[1])
        team[i[1]] = i[0]

    for i in range(len(visited)):
        if not visited[i]:
            dfs(tree, visited, i, order)

    for i in range(len(tree)):
        if tree[i]:
            answer[i] = min(tree[i] + [i], key=lambda x: sales[x])

    complete = {i: True if answer[i] == i else False for i in answer}

    for i in reversed(order):
        if not complete[i]:
            if sales[i] <= sales[answer[i]] + sales[answer[team[i]]]:
                answer[i] = answer[team[i]] = i
                complete[i] = complete[team[i]] = True
    return sum(map(lambda x: sales[x], set(answer.values())))

_sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
_links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# _sales = [5, 6, 5, 3, 4]
# _links = [[2, 3], [1, 4], [2, 5], [1, 2]]
# _sales = [5, 6, 5, 1, 4]
# _links = [[2, 3], [1, 4], [2, 5], [1, 2]]
# _sales = [10, 10, 1, 1]
# _links = [[3, 2], [4, 3], [1, 4]]


print(solution(_sales, _links))
