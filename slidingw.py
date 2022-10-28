#counts the number of divisible substring eg 240 -> 240/24 and 240/40
def sw(num, k):
    numstring=str(num)
    count = 0
    i=0
    #used orginal here cause numstring gets manipulated
    while i < len(str(num)):
        wind_rnge = numstring[:k] 
        if (len(wind_rnge) == k):
            if int(wind_rnge) > 0 and num % int(wind_rnge) == 0:
                count+=1
            numstring=numstring[1:]
            i+=1
            #print(wind_rnge)
        else:
            return count
    #print(count)
    return count

print(sw(30003, 3)) 
print(sw(430043, 2))
print(sw(240, 2))
