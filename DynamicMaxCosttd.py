td={}
def mp(n,p):
    if td.get((n),-1)!=-1:
        return td[n]
    if n==0:
        return 0
    else:
        q=-999999999999999
        for i in range(1,len(p)+1):
            if i<=n:
                q=max(q,p[i-1]+mp(n-(i),p))
        td[n]=q
        return q
if __name__=="__main__":
    import timeit
    n=int(input("Enter length of rod"))
    p=[1,5,8,9,10,17,17,20,24,30]
    start=timeit.default_timer()
    print(mp(n,p))
    end=timeit.default_timer()
    print(end-start)