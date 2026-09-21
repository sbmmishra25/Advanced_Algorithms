"""Backtracking and branch-and-bound teaching examples."""

def n_queens(n):
    cols=set();diag1=set();diag2=set();board=[];solutions=[]
    def place(r):
        if r==n:solutions.append(board[:]);return
        for c in range(n):
            if c in cols or r-c in diag1 or r+c in diag2:continue
            cols.add(c);diag1.add(r-c);diag2.add(r+c);board.append(c)
            place(r+1)
            board.pop();cols.remove(c);diag1.remove(r-c);diag2.remove(r+c)
    place(0);return solutions

def subsets(items):
    out=[]
    def go(i,cur):
        if i==len(items):out.append(cur[:]);return
        go(i+1,cur);cur.append(items[i]);go(i+1,cur);cur.pop()
    go(0,[]);return out

def permutations(items):
    a=list(items);out=[]
    def go(i):
        if i==len(a):out.append(a[:]);return
        for j in range(i,len(a)):
            a[i],a[j]=a[j],a[i];go(i+1);a[i],a[j]=a[j],a[i]
    go(0);return out

def graph_coloring(graph,k):
    nodes=list(graph);color={}
    def ok(u,c):
        return all(color.get(v)!=c for v in graph.get(u,[]))
    def go(i):
        if i==len(nodes):return True
        u=nodes[i]
        for c in range(k):
            if ok(u,c):
                color[u]=c
                if go(i+1):return True
                del color[u]
        return False
    return color if go(0) else None
