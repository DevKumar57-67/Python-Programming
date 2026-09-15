'''

def binary(n,key):
    low = 0
    high = len(n)-1
    while low <= high:
        mid = low + (high - low) //2
        if n[mid] == key:
            return mid
        elif n[mid] <  key:
            low = mid+1
        else:
            high = mid-1
    return -1

#Calling the function
n =list(map(int, input("Enter the array: ").split()))
key = int(input("Enter the key element to search:"))
result = binary(n,key)
print(result)

'''

#The binary search algorithm is only applicable on the sorted array

def binary_search(arr,n,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low+(high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1

#Calling the function
arr = list(map(int, input("Enter the elements of the array:").split()))
n = len(arr)
print("Th size of the array is:", n)
key = int(input("Enter the key elemnt of the array: "))
result = binary_search(arr, n , key)
print("The key element is on the index :", result )