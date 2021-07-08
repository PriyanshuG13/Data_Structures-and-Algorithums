def StackArray():
    class Stack:
        def __init__(self):
            self.top = 0
            self.stack = list()

        def push(self, data):
            self.top += 1
            self.stack.append(data)

        def pop(self):
            if self.top == 0:
                print("Stack Underflow")
            else:
                self.top -= 1
                return self.stack[self.top]

        def peek(self):
            if self.top == 0:
                print("Stack Underflow")
                return -1
            else:
                return self.stack[self.top+1]

        def size(self):
            return self.top+1

        def search(self, data):
            stack = self.stack
            if self.top == 0:
                print("Stack Underflow")
                return -1
            else:
                for i in range(self.top):
                    if data == stack[i]:
                        return i
                print("Value Not Found.")
                return -1

        def traverse(self):
            if self.top == 0:
                print("Stack Underflow")
            else:
                print("top", end="")
                for i in range(self.top-1, -1, -1):
                    print(" -", self.stack[i], end="")
                print()


    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.traverse()
    print(s.pop())
    print(s.search(2))
    s.traverse()

def StackLinkedList():
    class Node:
        def __init__(self, data=None):
            self.data, self.next = data, None

    class Stack:
        def __init__(self):
            self.top = 0
            self.head = None

        def push(self, data):
            New = Node(data)
            if self.head is not None:
                New.next = self.head
                self.head = New
                self.top += 1
            else:
                self.head = New
                self.top += 1

        def pop(self):
            if self.top == 0:
                print("Stack Underflow")
            else:
                top = self.head.data
                self.head = self.head.next
                self.top -= 1
                return top

        def peek(self):
            if self.top == 0:
                print("Stack Underflow")
            else:
                return self.head.data

        def size(self):
            return self.top

        def search(self, data):
            temp = self.head
            if self.top == 0:
                print("Stack Underflow")
            else:
                for i in range(1, self.top+1):
                    if data == temp.data:
                        return i
                    temp = temp.next
                print("Value Not Found.")
                return -1

        def traverse(self):
            temp = self.head
            if self.top == 0:
                print("Stack Underflow")
            else:
                print("top", end="")
                for i in range(self.top):
                    print(" ->", temp.data, end="")
                    temp = temp.next
                print()

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.traverse()
    print(s.pop())
    print(s.search(2))
    s.traverse()

# StackArray()
# StackLinkedList()
