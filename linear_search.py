def linear(n,key):
    for i in range(len(n)):
        if (n[i]==key):
            return i
    return -1

#Calling the function
n = list(map(int,input("Enter the  arrray elements: ").split()))
key = int(input("Enter the key element to search: "))
result = linear(n,key)
print(result)


