#Functions are very important in computer programming as they amke our code more modular and reusable
#In Python we make functions using the def keyword followed by the function name and arguements  

#A python sum function
def sum(a,b):
    return a+b

#Calling the function
a= int(input("Enter a:"))
b= int(input("Enter b:"))
result = sum(a,b)
print("The sum is:", result)
