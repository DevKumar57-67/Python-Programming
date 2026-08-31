def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

#Calling the Functiion

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

swap_num= swap(a,b)
print(swap_num)