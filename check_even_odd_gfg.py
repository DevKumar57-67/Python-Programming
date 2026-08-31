#This is a GeeksForGeeks logic building basic problem 


def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


#Calling the function
n = int(input("Enter the value to check:"))
check = check_even_odd(n)
print(check)


