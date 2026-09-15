#Array is a linear data structure that stores elements of the same type in a contiguous block of memory.
#It stores a fixed-size sequential collection of elements of the same type 

#Arrays in Python
arr = [1,2,3,4,5]
print(arr)
print(arr*2)

#Taking array as input 
arr= list(map(int,input("Enter the elements of the array:").split()))
print("The array is ", arr)

#operations on arrays
#finding the length of the array we use the len built-in function n python  
print("the length of the array is:", len(arr))

#Traversing the arrays 
#we use a for loop for array traversel
for i in arr:
    print(i)


#Merging two arrays
arr1 = list(map(int,input("Enter the array1:").split()))
arr2 = list(map(int,input("Enter the array2:").split()))

arr_merge = arr1+arr2
print("The mergd array s: ", arr_merge)


#Searching an element in ana array
#For searching an element in an array we use the two very important algorithms 
#Linear Search and Binary Search 
#Linear Search works for both sorted and unsorted arrays but Binary Search is only applicable on the sorted arrays

#Linear Search
#Linear search is a very important searching algorithm with time complexity O(n) and space complexity of O(1)

def linear_search(arr,n,key):
    for i in range(0,n):
        if arr[i] == key:
            return i
    return -1

#Calling the function
arr=list(map(int,input("Enter the elements of the array:").split()))
n = int(input("Enter the size of the array:"))
key = int(input("Enter the key element to find:"))
result = linear_search(arr,n,key)
print(result)

#Binary Search is also a searching algorithm which is more efficient than linear search 
#Time complexity of this algorithm is O(log n) and space complexity is O(1

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

#Binary search algorithm is only applicable on the sorteed array



#Sorting an Array
#Sorting an array is an important operation which is used to sort the elementsb of the array in whatever the condition is 
#We have a number of sorting algorithms to do this
# Bubble sort 
# Selection sort
# Insertion sort
# Merge Sort
# Quick Sort 
# Heap Sort
# Counting 
# Radix sort
# Bucket Sort


