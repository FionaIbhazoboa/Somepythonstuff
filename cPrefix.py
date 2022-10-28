def commonPrefix(mylist):
    output=""
    first=mylist[0]
    for i in range(len(first)):
        for s in mylist:
            #if i is at the end of string just return
            if i== len(s) or s[i] != mylist[0][i]:
                return output
        output += mylist[0][i]
    return output

mylist= ["flower","flow","flight"] 
#print(mylist[0][0]) 
print(commonPrefix(mylist))

