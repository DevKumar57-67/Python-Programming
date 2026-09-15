#Leetcode problem 21 states to merge two linked lists and store than in a thirs linked list

#If 
# l1 = [1,2,3]
# l2 = [1,2,4]
# merged_list = [1,1,2,2,3,4]

# Algorithm
# step1: make a dummy linked list 
# step2: compare both the linked list elements
# step3: store the elements one by one in sorted way
# step4: stop when the list is finised and return it


#code


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_list(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:

        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Attach the remaining nodes
    current.next = list1 if list1 else list2

    return dummy.next


# Creating first linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(4)

node1.next = node2
node2.next = node3

list1 = node1


# Creating second linked list
node4 = Node(1)
node5 = Node(3)
node6 = Node(4)

node4.next = node5
node5.next = node6

list2 = node4


# Merge the two lists
result = merge_list(list1, list2)


# Print the merged linked list
current = result

while current:
    print(current.data, end=" → ")
    current = current.next

print("None")