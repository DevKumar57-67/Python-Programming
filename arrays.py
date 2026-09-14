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