#Conditional Statements


def conditions(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are a minor."


#Calling the function

age = int(input("Enter the age:"))
result = conditions(age) 
print(result)
