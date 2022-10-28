def llist(lisst):
    
    newlist=[[] for i in range(len(lisst)-1)]
    i=0
    j=i+1
    k=0
    while i< len(lisst) and j <len(lisst):
        if newlist and lisst[i][0] <= newlist[-1][1]:
            newlist[-1][1]= max(lisst[i][1], newlist[-1][1])
        else:
            newlist.append(lisst[i])


            if lisst[i][k+1]>= lisst[j][k]:
                newlist[i].append(lisst[i][k])
                newlist[i].append(lisst[j][k+1])
            else:
                newlist[i].append(lisst[j][k])
                newlist[i].append(lisst[j][k+1])

            j+=1
            i+=1
    else:
        
        #newlist[i].append(lisst[i][k+1])

   # while i< len(lisst):
     #   newlist[i].append(lisst[i])
    return newlist 

print(llist([[1,3],[2,6],[8,10],[15,18]]))
print(llist([[1,4],[4,5]]))
print(llist([[1,4]]))
print(llist([[1,4],[5,6]]))