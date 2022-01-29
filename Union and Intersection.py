from collections import Counter


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
            if cur_head.next is not None:
                out_string += str(cur_head.value) + " -> "
            else:
                out_string += str(cur_head.value)
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


def union(llist_1, llist_2):
    all = set()
    node = llist_1.head
    while node:
        all.add(node.value)
        node = node.next
    node = llist_2.head
    while node:
        all.add(node.value)
        node = node.next
    sol_llist = LinkedList()
    for item in all:
        sol_llist.append(item)
    return sol_llist


def intersection(llist_1, llist_2):
    # using sets for efficiency
    values1 = set()
    values2 = set()
    node = llist_1.head
    while node:
        values1.add(node.value)
        node = node.next
    node = llist_2.head
    while node:
        values2.add(node.value)
        node = node.next
    intersection = LinkedList()
    for value in values1:
        if value in values2:
            intersection.append(value)
    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 10, 6, 4, 3, 1]
element_2 = [6, 10, 4, 9, 6, 1, 11, 21, 111]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# Expect 1 -> 2 -> 35 -> 3 -> 4 -> 6 -> 9 -> 10 -> 11 -> 111 -> 21
print(union(linked_list_1, linked_list_2))
# Expect 1 -> 4 -> 6 -> 10
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 6, 6, 4, 3, 23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# Expect 1 ->2 -> 35 -> 3 -> 4 -> 6 -> 23
print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))  # Expect empty 4