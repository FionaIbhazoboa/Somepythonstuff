def operation(operlist):
    mylist=[]
    newtemp=""
    mystack=[]
    mybool=False
    
    for i in range(len(operlist)):
        temp= operlist[i].split()
        if (temp[0]=="Insert"):
            value= newtemp+temp[1]
            mylist.append(value)
            #mylist="".join(mylist)
            newtemp=value
            

        elif(temp[0]=="Backspace"):
            value= mylist[-1][:-1]
            mylist.append(value)
            #mystack.append

        elif(temp[0]=="Undo"):
           # for j in 
            value=mylist[-2]
            mylist.append(value)



        

    #print(temp)



    return mylist



print(operation(["Insert boy", "Insert cat", "Insert milk", "Backspace", "Backspace", "Undo", "Undo", "Undo"]))
print(operation(["Insert cat","Insert dog","Undo"]))


#mylist= ["codesignal", "code"]

#print(mylist[0][:-1])
