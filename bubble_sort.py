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
