def toh(n, aux, src, des):
    if (n == 1):
        print("Move from", src, "to", des)
        return 
    else:
        toh(n-1, src, des, aux)
        print("Move from", src, "to", des)
        toh(n-1, aux, src, des)


#calling the function
n = int(input("Enter the number of disks:"))

tower = toh(n, 'A', 'B', 'C')
print(tower)
