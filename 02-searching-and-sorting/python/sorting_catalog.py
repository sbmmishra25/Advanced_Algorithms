"""Major sorting algorithms for study and comparison."""
from typing import List, MutableSequence

def bubble_sort(a: MutableSequence[int]) -> None:
    for end in range(len(a)-1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped: return

def insertion_sort(a: MutableSequence[int]) -> None:
    for i in range(1, len(a)):
        x=a[i]; j=i-1
        while j >= 0 and a[j] > x:
            a[j+1]=a[j]; j-=1
        a[j+1]=x

def selection_sort(a: MutableSequence[int]) -> None:
    for i in range(len(a)):
        m=min(range(i,len(a)), key=a.__getitem__)
        a[i],a[m]=a[m],a[i]

def merge_sort(a: List[int]) -> List[int]:
    if len(a)<=1: return a[:]
    m=len(a)//2
    left,right=merge_sort(a[:m]),merge_sort(a[m:])
    out=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]: out.append(left[i]); i+=1
        else: out.append(right[j]); j+=1
    return out+left[i:]+right[j:]

def quick_sort(a: MutableSequence[int]) -> None:
    def partition(lo,hi):
        pivot=a[hi]; p=lo
        for j in range(lo,hi):
            if a[j] <= pivot:
                a[p],a[j]=a[j],a[p]; p+=1
        a[p],a[hi]=a[hi],a[p]
        return p
    def sort(lo,hi):
        if lo>=hi:return
        p=partition(lo,hi); sort(lo,p-1); sort(p+1,hi)
    sort(0,len(a)-1)

def heap_sort(a: MutableSequence[int]) -> None:
    n=len(a)
    def sift(root,size):
        while 2*root+1<size:
            child=2*root+1
            if child+1<size and a[child+1]>a[child]: child+=1
            if a[root]>=a[child]: return
            a[root],a[child]=a[child],a[root]; root=child
    for i in range(n//2-1,-1,-1): sift(i,n)
    for end in range(n-1,0,-1):
        a[0],a[end]=a[end],a[0]; sift(0,end)

def counting_sort(a: List[int]) -> List[int]:
    if not a:return []
    lo,hi=min(a),max(a)
    if hi-lo>10_000_000: raise ValueError("key range too large")
    count=[0]*(hi-lo+1)
    for x in a: count[x-lo]+=1
    return [v for i,c in enumerate(count) for v in [i+lo]*c]

def radix_sort_nonnegative(a: List[int]) -> List[int]:
    if any(x<0 for x in a): raise ValueError("nonnegative integers only")
    out=a[:]; exp=1; mx=max(out,default=0)
    while mx//exp:
        buckets=[[] for _ in range(10)]
        for x in out: buckets[(x//exp)%10].append(x)
        out=[x for b in buckets for x in b]; exp*=10
    return out

if __name__=="__main__":
    data=[9,4,7,3,1,8,2,6,5]
    for fn in (bubble_sort,insertion_sort,selection_sort,quick_sort,heap_sort):
        x=data[:]; fn(x); print(fn.__name__,x)
    print("merge_sort",merge_sort(data))
    print("counting_sort",counting_sort(data))
    print("radix_sort",radix_sort_nonnegative(data))
