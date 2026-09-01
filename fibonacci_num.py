def fib(n):
    if (n == 0 or n ==1):
        return n
    else:
        return fib(n-1) + fib(n-2)

#Calling the function
n = int(input("Enter the number:"))
fibo=fib(n)
print("Fibonacci number is:", fibo)
