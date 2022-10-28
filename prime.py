def prim(N):
    #N=10
    for i in range(2, N):
        if N % i == 0:
            break
    else: 
        return ("yes")

print(prim(9))

def primr(N):
    res=[]
    for i in range(1, N+1):
        if i == 1:
            continue
            #res.append(i)
        else:
            for j in range(2, i):
                if i % j == 0: # that is not a fraction
                    break
            else:
                res.append(i)
    return res


print(primr(9))