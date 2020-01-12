bt={0:0}
def mp(n,p):
    for j in range(1,n+1):
        q=-999999999
        for i in range(1,len(p)+1):
            if j>=i:
                q=max(q,p[i-1]+bt[j-i])
        bt[j]=q
    return bt[n]
if __name__=="__main__":
    import timeit
    n=int(input("Enter length of rod"))
    p=[1,5,8,9,10,17,17,20,24,30]
    start=timeit.default_timer()
    print(mp(n,p))
    end=timeit.default_timer()
    print(end-start)