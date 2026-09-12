#Tower Of Hanoi 
'''
def toh(n, src, aux, des):
    if(n ==1):
        return 
    else:
        toh(n-1, src, des, aux)
    return toh(n-1, aux,src,des)

#Calling the function

n = int(input("Enter the number of discs:"))
result = toh(n, 'A', 'B', 'C')
print(result)

'''

def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Number of disks
n = int(input("Enter the number of discs:"))

result =tower_of_hanoi(n, 'A', 'B', 'C')
print(result)
