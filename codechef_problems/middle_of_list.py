# Finding the middle element of the list 
# We use the two pointer technique fats and slow pointer pointer


# Algorithm:
# step1: we use two pointers slkow and fast fast moves twice of slow and when fast reaches the end slow is at half
# step2: then use a while loop fast and fast.next 
# step3: then make the pointers equal to the value


#code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def middle_element(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

print(middle_element(head))