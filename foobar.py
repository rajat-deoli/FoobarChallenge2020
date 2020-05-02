def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        



def solution(i):
    # Your code here
    str1=""
    
    for n in range(1,30000):
        if prime(n)==True:
            str1+=str(n)
    
    
    return str1[i:i+5]




