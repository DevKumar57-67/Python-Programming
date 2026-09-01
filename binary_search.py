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
            high = mid+1
    return -1

#Calling the function
n =list(map(int, input("Enter the array: ").split()))
key = int(input("Enter the key element to search:"))
result = binary(n,key)
print(result)
