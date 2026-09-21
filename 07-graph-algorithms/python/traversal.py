from collections import deque

def bfs(graph, start):
    seen, order = {start}, []
    q = deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order

def dfs(graph, start):
    seen, order = set(), []
    def visit(u):
        seen.add(u); order.append(u)
        for v in graph[u]:
            if v not in seen:
                visit(v)
    visit(start)
    return order

if __name__ == "__main__":
    g = {0:[1,2], 1:[0,3], 2:[0], 3:[1]}
    print(bfs(g, 0))
    print(dfs(g, 0))