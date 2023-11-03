class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.data

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            removed_node = self.head
            self.head = removed_node.next
            if not self.head:
                self.tail = None
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            removed_node = current_node.next
            current_node.next = removed_node.next
            if not current_node.next:
                self.tail = current_node
        self.length -= 1
        return removed_node.data

    def insert(self, n, val):
        if n < 0 or n > self.length:
            return None
        if n == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        elif n == self.length:
            self.push(val)
        else:
            current_node = self.head
            for i in range(n-1):
                current_node = current_node.next
            new_node = Node(val)
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next


example_list = LinkedList()
example_list.push(1)
example_list.push(2)
example_list.push(3)
example_list.insert(1, 4)
example_list.remove(2)

for item in example_list:
    print(item) 