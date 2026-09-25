'''
Problem statement
You are given an integer ‘NUM’ . Your task is to find out whether this number is an Armstrong number or not.

A k-digit number ‘NUM’ is an Armstrong number if and only if the k-th power of each digit sums to ‘NUM’.

Example
153 = 1^3 + 5^3 + 3^3.

Therefore 153 is an Armstrong number.


'''

#Algorithm:
# Step1: store the number 
# Step2: count digits
# step3: extract each digit by using this d = n % 10 then make digit ** digit then remove the last digit d // = 10

# Code:

n = int(input("Enter the number:"))

original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("true")
else:
    print("false")