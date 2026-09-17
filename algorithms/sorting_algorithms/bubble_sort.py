#Bubble sort is a classic sorting algorithm used to sort elements in an array

#Algorithm:
# step1: we take the first element of the array as a bubble element
# step2: then we compare the bubble element with  the adjacent element 
# step3: now if the bubble elemnt is > adjacent elet then swap it else shift the bubble ahead
# step4: keep on doing this till you find the sorted array an return the array
# step5: return the complete array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Calling the function 

arr = list(map(int, input("Enter the array:").split()))
result = bubble_sort(arr)
print("The sorted array is: ", result)


