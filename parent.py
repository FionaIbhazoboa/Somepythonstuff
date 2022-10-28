def param(s):
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    mystack = []
    for i in range(len(s)):
        if(mystack==[]):
            mystack.append(s[i])
        else:
            if (mystack[-1] in opening and s[i] in closing and closing.index(s[i]) == opening.index(mystack[-1])):
                mystack.pop()
            else: 
                mystack.append(s[i])
                
    return True if not mystack else False

s = "([])"
print(param(s))
