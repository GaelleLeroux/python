def MultiplicationMatrice():
    u=[[1,2,3,3],[3,0,0,1],[4,0,1,0],[7,4,4,4]]
    v=[[1,0,0,0],[2,0,1,7],[3,1,0,9],[7,4,4,4]]
    L=[]
    M=[]
    if len(u[0])!=len(v):
        return("on ne peut pas muliplier ses matrices")
    else:
        for i in range(0,len(u)):
            M=[]
            for s in range(0,len(v[0])):
                p=0
                for o in range(0,len(v)):
                    y=0
                    y=u[i][o]*v[o][s]
                    p=p+y
                M.append(p)
            L.append(M)
        return(L)