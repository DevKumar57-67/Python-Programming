#Binary Search is an efficient searching algorithm and is frequently preffered over linear search
#Binary search has a drawback it is only applicable on a sorted array

#Algorithm: 
# step1: divide the array in two halves
# step2: find the mid element if mid == key then return it
# Step3: if mid < key then proceed to the seconf part of the array
# step4: if mid > key then procedd the the first part of the array
# step5: keep on doing it  until the key element is found then return it 


def binary_search( n , key):
    low = 0
    high = len(n)-1
    while ( low <= high):
         mid = low+(high-low)//2
         if n[mid] == key:
              return mid
         elif n[mid] < key:
              low = mid+1
         else:
              high = mid-1
    return -1

        
         

#Calling the function

n  = list(map(int, input("Enter the array:").split()))
key = int(input("Enter the key element"))
result = binary_search(n, key)
print("The Key elemnt is:", result)