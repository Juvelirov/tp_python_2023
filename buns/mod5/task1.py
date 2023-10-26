class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.head.data

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next


stack = Stack()

stack.push(5)
stack.push(2)
stack.push(9)
stack.push(3)

stack.print_stack()

print("Stack vertex value:", stack.peek())
print("Removed an item from the stack:", stack.pop())
print("Removed an item from the stack:", stack.pop())

stack.print_stack()