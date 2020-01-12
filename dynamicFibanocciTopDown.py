td={}
td[0]=0
td[1]=1

def tdfib(n):
    """Top down approach for dynamic programming"""
    if td.get(n,-1)==-1:
        td[n]=tdfib(n-1)+tdfib(n-2)
        return td[n]
    else:
        return td[n]

if __name__=="__main__":
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(tdfib(n))
    print(td)
    end=timeit.default_timer()
    print("Time taken in seconds is ",end-start)