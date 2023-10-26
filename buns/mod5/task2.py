class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev_elem = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_elem = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
