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
def tdgrid(i,j,b1,b2):
    if d.get((i,j),-1)==-1:
        if i==b1 and j==b2:
            return 0
        if i==0 and j==0:
            return 1
        elif i==0:
            return tdgrid(0,j-1,b1,b2)
        elif j==0:
            return tdgrid(i-1,0,b1,b2)
        else:
            return tdgrid(i-1,j,b1,b2)+tdgrid(i,j-1,b1,b2)
    else:
        return d[(i,j)]
    
if __name__=='__main__':
    i=int(input())
    j=int(input())
    b1=int(input())
    b2=int(input())
    import timeit
    start=timeit.default_timer()
    print(tdgrid(i,j,b1,b2))
    end=timeit.default_timer()
    print("Time taken in seconds for iteration ",end-start)
    print(d)