def isPalindrome(x):
    revers=0
    check=x
    while x > 0:
        revers= (revers*10) + (x%10)
        x//=10
    print(revers)
    print(check)
    return check==revers    


print(isPalindrome(121))