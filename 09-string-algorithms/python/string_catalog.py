"""Core exact string algorithms."""

def prefix_function(s):
    pi=[0]*len(s)
    for i in range(1,len(s)):
        j=pi[i-1]
        while j and s[i]!=s[j]:j=pi[j-1]
        if s[i]==s[j]:j+=1
        pi[i]=j
    return pi

def kmp_search(text,pattern):
    if not pattern:return list(range(len(text)+1))
    pi=prefix_function(pattern);j=0;out=[]
    for i,ch in enumerate(text):
        while j and ch!=pattern[j]:j=pi[j-1]
        if ch==pattern[j]:j+=1
        if j==len(pattern):
            out.append(i-j+1);j=pi[j-1]
    return out

def z_function(s):
    z=[0]*len(s);l=r=0
    for i in range(1,len(s)):
        if i<=r:z[i]=min(r-i+1,z[i-l])
        while i+z[i]<len(s) and s[z[i]]==s[i+z[i]]:z[i]+=1
        if i+z[i]-1>r:l,r=i,i+z[i]-1
    if s:z[0]=len(s)
    return z

def rabin_karp(text,pattern,base=911382323,mod=1_000_000_007):
    n,m=len(text),len(pattern)
    if m==0:return list(range(n+1))
    if m>n:return []
    hp=ht=0; power=pow(base,m-1,mod);out=[]
    for i in range(m):
        hp=(hp*base+ord(pattern[i]))%mod
        ht=(ht*base+ord(text[i]))%mod
    for i in range(n-m+1):
        if ht==hp and text[i:i+m]==pattern:out.append(i)
        if i<n-m:
            ht=(ht-ord(text[i])*power)%mod
            ht=(ht*base+ord(text[i+m]))%mod
    return out
