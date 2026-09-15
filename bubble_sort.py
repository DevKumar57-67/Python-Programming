#Bubble sort is an important sorting algorithm used to sort the elemenst of the array
#Algorithm  
# step 1: traverse the array using a nested for loop first loop uns for n-1, second loop n-1-i
# step 2: then check if arr[j] > arr[j+1] compare the element with the adjacent element 
# step 3: if yes: then swap the elements if no: shift the bubble
# step 4: return the array


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


#Calling the function
arr = list(map(int, input("Enter the array:").split()))
sorted= bubble(arr)
print("Sorted array is:", sorted)

#Time complexity of the Bubble sort algorithm is O(n^2)
#Space complexity of the bubble sort algorithm O(1) 

