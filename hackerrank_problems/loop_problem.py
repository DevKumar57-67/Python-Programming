#This is a basic hackerrank problem 

'''
Task

For each integer  in the interval  (given as input) :

If , then print the English representation of it in lowercase. That is "one" for , "two" for , and so on.
Else if  and it is an even number, then print "even".
Else if  and it is an odd number, then print "odd".
Input Format

The first line contains an integer, .
The seond line contains an integer, .

Constraints


Output Format

Print the appropriate English representation,even, or odd, based on the conditions described in the 'task' section.

Note: 

'''

#algorithm:
# step 1: use a for loop n =a, n <=b, n++
# step 2: use if case and elif case
# step 3: use conditional statements 

# code

n = int(input("Enter the value of n:"))
a , b = list(map,int(input().split()))


for n in range(a, b+1):
    if (n ==1):
        print("one")
    elif (n ==2):
        print("two")
    elif (n ==3):
        print("three")
    elif (n ==4):
        print("four")
    elif (n ==5):
        print("five")
    elif (n ==6):
        print("six")
    elif (n ==7):
        print("seven")
    elif (n ==8):
        print("eight")
    elif (n == 9):
        print("nine")
    elif n % 2==0:
        print("even")
    else:
        print("odd")




    
    
