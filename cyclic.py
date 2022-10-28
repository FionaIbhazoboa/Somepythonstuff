def cyclic(arr):
    i=0
    #get min value
    x=min(arr)
    while(i<len(arr)):
        #we need index to check if the value at i is in the right pos
        index=arr[i]-x
        #if the value - the min is not = to the index, swap
        if (i != arr[i]-x):
            arr[i], arr[index] = arr[index], arr[i]
        else:
            i +=1
    return arr

arr= [13, 14, 16, 12, 11, 15]
#newarr=[6,2,7,8,1] 
#print(cyclic(arr))
print(cyclic(arr))
