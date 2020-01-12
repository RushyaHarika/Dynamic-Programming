bu={0:0}
def buch(l,v):
    """Bottom up approach for finding minimum number of coins in Dynamic Programming"""
    for i in range(1,v+1):
        bu[i]=sys.maxsize
    for value in range(1,v+1):
        for x in l:
            if x<=value:
                s=bu[value-x]
                if s+1<bu[value]:
                    bu[value]=s+1
    return bu[v]
if __name__=="__main__":
    import sys
    import timeit
    v=int(input())
    l=eval(input())
    start=timeit.default_timer()
    print(buch(l,v))
    end=timeit.default_timer()
    print(end-start)