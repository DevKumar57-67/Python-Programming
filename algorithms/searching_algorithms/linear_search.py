#Linear Search is a classic searching algorithm


# Algorithm: 
# Step1: traverse the whole array
# Step2: than check if arr[i] == key element
# Step3: the return the index

def linear_search(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

#Calling the function
arr = list(map(int, input("Enter the elements of the array: ").split()))
n = len(arr)
print("The size of the arrat is: ",n)
key = int(input("Enter the key element:"))
result = linear_search(arr,n,key)
print("The key element is at index: ", result)

#Linear Search has a time complexity of O(n) and space complexity of O(1) 

