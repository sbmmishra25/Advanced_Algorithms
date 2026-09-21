"""Shortest-path and max-flow teaching implementations."""

from heapq import heappush, heappop
from collections import deque

def dijkstra(graph, source):
    dist={u:float("inf") for u in graph}; parent={source:None}; dist[source]=0
    pq=[(0,source)]
    while pq:
        d,u=heappop(pq)
        if d!=dist[u]:continue
        for v,w in graph.get(u,[]):
            nd=d+w
            if nd<dist.get(v,float("inf")):
                dist[v]=nd; parent[v]=u; heappush(pq,(nd,v))
    return dist,parent

def bellman_ford(n, edges, source):
    inf=float("inf"); d=[inf]*n; p=[None]*n; d[source]=0
    for _ in range(n-1):
        changed=False
        for u,v,w in edges:
            if d[u]!=inf and d[u]+w<d[v]:
                d[v]=d[u]+w;p[v]=u;changed=True
        if not changed:break
    for u,v,w in edges:
        if d[u]!=inf and d[u]+w<d[v]: raise ValueError("reachable negative cycle")
    return d,p

def floyd_warshall(dist):
    d=[row[:] for row in dist]; n=len(d)
    for k in range(n):
        for i in range(n):
            if d[i][k]==float("inf"):continue
            for j in range(n):
                if d[k][j]!=float("inf"):
                    d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

class MaxFlow:
    def __init__(self,n):
        self.g=[[] for _ in range(n)]
    def add_edge(self,u,v,c):
        self.g[u].append([v,c,len(self.g[v])])
        self.g[v].append([u,0,len(self.g[u])-1])
    def max_flow(self,s,t):
        flow=0;n=len(self.g)
        while True:
            parent=[None]*n;q=deque([s]);parent[s]=(-1,-1)
            while q and parent[t] is None:
                u=q.popleft()
                for i,e in enumerate(self.g[u]):
                    v,c,rev=e
                    if c>0 and parent[v] is None:
                        parent[v]=(u,i);q.append(v)
                        if v==t:break
            if parent[t] is None:return flow
            aug=float("inf");v=t
            while v!=s:
                u,i=parent[v];aug=min(aug,self.g[u][i][1]);v=u
            v=t
            while v!=s:
                u,i=parent[v]; e=self.g[u][i]; rev=e[2]
                e[1]-=aug; self.g[v][rev][1]+=aug; v=u
            flow+=aug
