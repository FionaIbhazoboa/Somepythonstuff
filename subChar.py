arr="abcabcbb"
l, res=0, 0
charSet=set()
print(len(arr))

for i in range(len(arr)):
    while arr[i] in charSet:
        charSet.remove(arr[l])
        l+=1
    charSet.add(arr[i])
    res=max(res, i-l+1)
print(res)

