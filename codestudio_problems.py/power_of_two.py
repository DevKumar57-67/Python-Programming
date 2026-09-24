'''

Problem statement
You have been given an integer 'N'.



Your task is to return true if it is a power of two. Otherwise, return false.



An integer 'N' is a power of two, if it can be expressed as 2 ^ 'K' where 'K' is an integer.



For example:
'N' = 4,
4 can be represented as 2^2. So, 4 is the power of two, and hence true is our answer.



'''

def isPowerOfTwo(n:int) -> bool:
    # Write your code here
    if n <= 0:
        return False
    while n % 2== 0:
        n //= 2
    return n ==1

#Calling the function

n = int(input("Enter the integer:"))
result = isPowerOfTwo(n)
print(result)

