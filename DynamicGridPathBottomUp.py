"""def grid(i,j,b1,b2):
    if i==b1 and j==b2:
        return 0
    if i==0 and j==0:
        return 1
    elif i==0:
        return grid(0,j-1,b1,b2)
    elif j==0:
        return grid(i-1,0,b1,b2)
    else:
        return grid(i-1,j,b1,b2)+grid(i,j-1,b1,b2)"""
d={}
d[(0,0)]=1#table creation
def btgrid(i,j):
    """filling the first column"""
    for c in range(1,j+1):
        d[(0,c)]=1
    """filling the first row"""
    for r in range(1,i+1):
        d[(r,0)]=1
    for r in range(1,i+1):
        for c in range(1,j+1):
            d[(r,c)]=d[(r-1,c)]+d[(r,c-1)]
    return d[(i,j)]
if __name__=='__main__':
    i=int(input())
    j=int(input())
    import timeit
    start=timeit.default_timer()
    print(btgrid(i,j))
    end=timeit.default_timer()
    print("Time taken in seconds for iteration ",end-start)
    print(d)