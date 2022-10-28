def add(a, b):
    #convert to decimal 
    a= int(a,2)
    b=int(b,2)
    sum = a+b
    sum = bin(sum).replace("0b", "")
    return sum





a ="11"
b="1"
print(add(a, b))