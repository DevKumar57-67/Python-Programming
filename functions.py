#Functions are very important in computer programming as they amke our code more modular and reusable
#In Python we make functions using the def keyword followed by the function name and arguements  

#A python sum function
def sum(a,b):
    return a+b

#Calling the function


#A Basic Calculator using python functions


def diff(a,b):
    return a-b


def prod(a,b):
    return a*b


def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def floatdiv(a,b):
    return a//b


#Calling the Function

a= int(input("Enter a:"))
b= int(input("Enter b:"))
add = sum(a,b)
minus  = diff(a,b)
mul = prod(a,b)
divide = div(a,b)
modulo = mod(a,b)
floatdivi= floatdiv(a,b)

print("The sum is:", add)
print("The diff is:", minus)
print("The prod is:", mul)
print("The division is:", divide)
print("The modulo is:", modulo)
print("The floatdiv is:", floatdivi)
