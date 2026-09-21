"""Searching and selection algorithms for study."""
from bisect import bisect_left,bisect_right
from typing import Sequence,Optional

def linear_search(a: Sequence[int], target:int)->Optional[int]:
    for i,x in enumerate(a):
        if x==target:return i
    return None

def binary_search(a: Sequence[int], target:int)->Optional[int]:
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==target:return m
        if a[m]<target:lo=m+1
        else:hi=m-1
    return None

def lower_bound(a:Sequence[int],target:int)->int:return bisect_left(a,target)
def upper_bound(a:Sequence[int],target:int)->int:return bisect_right(a,target)

def jump_search(a:Sequence[int],target:int)->Optional[int]:
    n=len(a)
    if not n:return None
    step=max(1,int(n**0.5)); prev=0
    while prev<n and a[min(prev+step,n)-1]<target:prev+=step
    for i in range(prev,min(prev+step,n)):
        if a[i]==target:return i
    return None

def exponential_search(a:Sequence[int],target:int)->Optional[int]:
    if not a:return None
    if a[0]==target:return 0
    bound=1
    while bound<len(a) and a[bound]<target:bound*=2
    lo,hi=bound//2,min(bound,len(a)-1)
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==target:return m
        if a[m]<target:lo=m+1
        else:hi=m-1
    return None

def interpolation_search(a:Sequence[int],target:int)->Optional[int]:
    lo,hi=0,len(a)-1
    while lo<=hi and a[lo]<=target<=a[hi]:
        if a[lo]==a[hi]:return lo if a[lo]==target else None
        pos=lo+(target-a[lo])*(hi-lo)//(a[hi]-a[lo])
        if a[pos]==target:return pos
        if a[pos]<target:lo=pos+1
        else:hi=pos-1
    return None

def quickselect(a:list[int],k:int)->int:
    if not 0<=k<len(a):raise IndexError("k out of range")
    lo,hi=0,len(a)-1
    while lo<=hi:
        pivot=a[hi]; p=lo
        for j in range(lo,hi):
            if a[j]<=pivot:a[p],a[j]=a[j],a[p];p+=1
        a[p],a[hi]=a[hi],a[p]
        if p==k:return a[p]
        if p<k:lo=p+1
        else:hi=p-1
    raise RuntimeError("unreachable")

def binary_search_on_answer(lo:int,hi:int,feasible)->int:
    while lo<hi:
        mid=(lo+hi)//2
        if feasible(mid):hi=mid
        else:lo=mid+1
    return lo
