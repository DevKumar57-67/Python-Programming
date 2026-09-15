#Selection sort is also a comparison based algorithm used to sort the elements of the array 

#Selection Sort finds the minimum element and places it at the correct position.

#Algorithm
# step 1: divide the array in two parts sorted and unsorted arrays
# step 2: select the minimum element in the unsorted array store it in the sorted part now that element is permanently sorted 
# step 3: select the next minimum element in the unsorted array then store it in the sorted partn
# step 4: keep on doing this till all the unsorted array becomes 0
# step 5: return the complete array


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


#Calling the function 
arr = list(map(int, input("Enter the elements off the array:").split()))
n = len(arr)
print("The size of the array is:", n)
result = selection_sort(arr)
print("The sorted array is:", result)


# The time complexity of selection sort algorithm is O(n^2)
# The space complexity of selection sort algorithm is O(1)
