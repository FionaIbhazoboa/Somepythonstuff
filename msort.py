def msort(arr):
    #loop is necessary so it doesnt recursive call 1 number in arr
    if len(arr) > 1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        msort(l)
        msort(r)

    #where i is left array indices and j is for right
    # and k is for new array 
        i=j=k=0 

    #will stop when eith hits the limit
        while i <len(l) and j < len(r):
            if l[i]< r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        #if there are extras handle it
        while i< len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j< len(r):
            arr[k]=r[j]
            j+=1
            k+=1

arr=[38, 27, 43, 3, 9, 82, 10]

for i in range(len(arr)):
    print(arr[i], end=" ")
print()
msort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
