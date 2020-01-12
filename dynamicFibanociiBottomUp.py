
"""def refib(n):
    if n==0 or n==1:
        return n
    else:
        return refib(n-1)+refib(n-2)"""
d={}
d[0]=0
d[1]=1
def btfib(n):
    """ *Dictionaries are used for fast access
        *bottom up approach for dynamic programming
        *dependencies must be priorly known"""
    for i in range(2,n+1):
        r=d[i-1]+d[i-2]
        d[i]=r
    ret=d[n]
    return ret

if __name__=='__main__':
    n=int(input())
    import timeit
    start=timeit.default_timer()
    a=btfib(n)
    end=timeit.default_timer()
    print("Time taken in seconds for ",end-start)
    print(a)