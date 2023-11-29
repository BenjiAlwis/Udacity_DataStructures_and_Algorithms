class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    list1 = []
    list2 = []
    node = llist_1.head
    while node is not None and node.next:
        list1.append(node.value)
        node = node.next
    node = llist_2.head
    while node is not None  and node.next:
        list2.append(node.value)
        node = node.next
    new_list = list(set(list1+list2))
    new_llist = LinkedList()
    for element in new_list:
        new_llist.append(element)
        
    return new_llist

def intersection(llist_1, llist_2):
    list1 = []
    list2 = []
    node = llist_1.head
    while node is not None and node.next:
        list1.append(node.value)
        node = node.next
    node = llist_2.head
    while node is not None and  node.next:
        list2.append(node.value)
        node = node.next
    new_list1 = list(set(list1))
    new_llist = LinkedList()
    for element in new_list1:
        if element in list2:
            new_llist.append(element)  
       
    return new_llist
    
    


# Test case 1
print("Test Case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
print("Test Case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
print("Test Case 3")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = ['a','c','s','h','a','g','x','d','e','s']
element_2 = ['s','z','a','e','f','w','v']

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Edge case 1
print("Edge Case 1")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = ['a','','s','h','a','g','x','d','e','']
element_2 = ['s','z','-','e','f','','v']

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Edge case 2

print("Edge Case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = ['a','','s','h','a','g','x','d','e','']
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Edge case 3

print("Edge Case 3")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


