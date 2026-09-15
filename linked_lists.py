#Linked Lists are a linear data structures which are used to store data dynamically with no contiguous memory allocations
#Arrays have a simple drawback that they are not dynamic and no address that issue we use linked lists which are dynamic

#Types of Linked Lists

# There are mainly three types of linked lists
# singly linked lists
# doubly linked lists
# circular linked lists


# singly linked lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Creating the linked lists
head = Node(10)
# Linking the list
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# printing the linked list
temp = head
while temp is not None:
    print(temp.data, end =" ")
    temp = temp.next