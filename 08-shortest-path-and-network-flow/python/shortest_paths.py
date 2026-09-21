from heapq import heappush, heappop

def dijkstra(graph, source):
    dist = {u: float("inf") for u in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            if w < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist

if __name__ == "__main__":
    g = {0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
    print(dijkstra(g, 0))