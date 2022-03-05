from collections import defaultdict
def solution(tickets):
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    for key in routes:
        routes[key].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return path[::-1]
