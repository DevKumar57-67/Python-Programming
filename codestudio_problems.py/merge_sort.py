'''
Problem statement
Given a sequence of numbers ‘ARR’. Your task is to return a sorted sequence of ‘ARR’ in non-descending order with help of the merge sort algorithm.

Example :

Merge Sort Algorithm -

Merge sort is a Divide and Conquer based Algorithm. It divides the input array into two-parts, until the size of the input array is not ‘1’. In the return part, it will merge two sorted arrays a return a whole merged sorted array.

'''

'''
Merge sort is a classic divide and conquer, two pointer technique and recursion based algorithm
In merge sort we divide the array in two parts and then keep on dividing it till we get the single  element then we compare the elements and sort them and finally merge them back

'''

def merge(l, r):
    res = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):

        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1

    return res


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr = list(map(int, input("Enter the array: ").split()))

result = merge_sort(arr)

print("The sorted array is:", result)