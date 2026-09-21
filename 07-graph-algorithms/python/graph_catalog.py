"""Core graph algorithms: BFS, DFS, topological sort, SCC, bridges, bipartite."""

from collections import deque

def bfs(graph, source):
    dist={source:0}; parent={source:None}; q=deque([source])
    while q:
        u=q.popleft()
        for v in graph.get(u,[]):
            if v not in dist:
                dist[v]=dist[u]+1; parent[v]=u; q.append(v)
    return dist,parent

def dfs(graph):
    seen=set(); order=[]
    def visit(u):
        seen.add(u); order.append(u)
        for v in graph.get(u,[]):
            if v not in seen: visit(v)
    for u in graph: 
        if u not in seen: visit(u)
    return order

def topological_sort(graph):
    indeg={u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indeg.setdefault(v,0); indeg[v]+=1
    q=deque(u for u,d in indeg.items() if d==0); out=[]
    while q:
        u=q.popleft(); out.append(u)
        for v in graph.get(u,[]):
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    if len(out)!=len(indeg): raise ValueError("graph contains a cycle")
    return out

def bipartite(graph):
    color={}
    for s in graph:
        if s in color: continue
        color[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in graph.get(u,[]):
                if v not in color: color[v]=color[u]^1;q.append(v)
                elif color[v]==color[u]: return False
    return True

def kosaraju_scc(graph):
    nodes=set(graph)
    for u in graph:nodes.update(graph[u])
    rev={u:[] for u in nodes}
    for u in graph:
        for v in graph[u]:rev[v].append(u)
    seen=set(); finish=[]
    def dfs1(u):
        seen.add(u)
        for v in graph.get(u,[]):
            if v not in seen:dfs1(v)
        finish.append(u)
    for u in nodes:
        if u not in seen:dfs1(u)
    seen.clear(); comps=[]
    def dfs2(u,c):
        seen.add(u);c.append(u)
        for v in rev[u]:
            if v not in seen:dfs2(v,c)
    for u in reversed(finish):
        if u not in seen:
            c=[];dfs2(u,c);comps.append(c)
    return comps
