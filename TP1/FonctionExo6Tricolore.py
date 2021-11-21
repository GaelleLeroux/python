def tricolore(n):
    u=0
    p=n
    while p!=int(p):
        p=p*10
    while p!=0:
        u=p%10
        p=p//10
        if u!=9 and u!=4 and u!=1:
            return(False)
    return(True)


def tous_les_tricolores(N):
    L=[]
    for i in range(0,N+1):
        if tricolore(i)==True:
            L.append(i)
    return(L)