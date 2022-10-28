def concat(n, x):
    count = 0
    i=0
    j=len(n)-1
    while i < len(n)-1:
        value=int(str(n[i])+ str(n[i+1]))
        print("This is "+ str(i) + " through loop. Value is "+ str(value))
        if value== x:
            count+=1
        else:
            value=int(str(n[i+1])+ str(n[i]))
            print("For else case This is "+ str(i) + " through loop. Value is "+ str(value))
            if value == x:
                count+=1
        i+=1
    while j > 0:
        value=int(str(n[j])+ str(n[j-1]))
        print("Backwards case This is "+ str(j) + " through loop. Value is "+ str(value))
        if value== x:
            count+=1
        j-=1


    return count


#print(concat([11,11,110], 11011)) #2 11=2 110=1
#print(concat([1, 212, 12, 12, 22], 1212)) #3  1=1 , 212=1, 12=2, 22=1
print(concat([777,77,77,7], 7777))
