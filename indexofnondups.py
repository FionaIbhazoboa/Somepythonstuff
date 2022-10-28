def iond(mystring):
    mydict = {}
    count=1
    for i in range(len(mystring)):
        if(mystring[i] not in mydict):
            mydict[mystring[i]]=[count, i] #{'l': [2, 2], 'o': [2, 2], 'v': [1, 2], 'e': [4, 4], 't': [1, 7], 'c': [1, 8], 'd': [1, 10]}
        else:
            temp = mydict.get(mystring[i])
            mydict[mystring[i]]=[temp[0]+1 for x in temp] #Add one to count
    for k in mydict:
        if(mydict[k][0]==1):
            return mydict[k][1]
       
    print(mydict) 
    return -1
       # else:
         #   return -1
    
    

print(iond("payment"))