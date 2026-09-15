#Linked Lists are a linear data structures which are used to store data dynamically with no contiguous memory allocations
#Arrays have a simple drawback that they are not dynamic and no address that issue we use linked lists which are dynamic

#Types of Linked Lists

# There are mainly three types of linked lists
# singly linked lists
# doubly linked lists
# circular linked lists

# Applications of linked lists 
# linked lists are used to solve polynomial arithmatic and sparse matrices representation and efficiently store values
# singly linked lists
'''
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


 # Operations on linked lists


'''















# Circular Linked Lists



# Operations in linked lists

# Traversing a Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(head):
    current = head

    while current:
        print(current.data, end=" → ")
        current = current.next

    print("None")


# Making the linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

traverse(node1)

# Insering a node at the beginning
# Inserting a node at the end  
# Inserting a node at specific index
# Deleting a node
# merging two linked lists
# size of linked lists both singly and doubly 


