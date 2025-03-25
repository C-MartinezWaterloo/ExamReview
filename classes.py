

class Queue:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.insert(0, items)

    def get(self,item):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)



class Stack:

    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def get(self):
        return self.items.pop()

    def is_empty(self):
        len(self.items) == 0

    def size(self):
        return len(self.items)


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, index: int, data):
        if index >= self.length or index < 0:
            print("Invalid Index")
            return
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                curr.next, new_node.next = new_node, curr.next
        self.length += 1
    
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
        return False

    def remove(self, data):
        '''Remove the first node with data == data in the list'''
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next is not None and curr.next.data != data:
            curr = curr.next
        if curr.next is None:
            print("Error: Failed to remove from the list")
            return
        curr.next = curr.next.next

    
    def print_list(self):
        s = "["
        curr = self.head
        while curr:
            s += f"{curr.data}, "
            curr = curr.next
        s = s[:-2] + "]"
        print(s)


