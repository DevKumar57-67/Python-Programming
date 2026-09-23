'''
Problem statement
You are given an array “ARR” of size N. Your task is to find out the sum of maximum and minimum elements in the array.

Follow Up:
Can you do the above task in a minimum number of comparisons?


'''


#Algorithm: use the min and max built in python function

def return_min_max(arr):
    return min(arr) + max(arr)

#Calling the function

arr = list(map(int, input("Enter the array:").split()))
siz = len(arr)
result = return_min_max(arr)
print("The sum of  min and max values is:",result)