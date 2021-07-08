def QueueArray():
    class Queue:
        def __init__(self):
            self.size = 0
            self.queue = list()

        def EnQueue(self, data):
            self.size += 1
            self.queue.append(data)

        def DeQueue(self):
            if self.size == 0:
                print("Queue Underflow")
            else:
                front = self.queue[0]
                self.queue.pop(0)
                self.size -= 1
                return front

        def size(self):
            return self.size

        def search(self, data):
            queue = self.queue
            if self.size == 0:
                print("Queue Underflow")
                return -1
            else:
                for i in range(self.size):
                    if data == queue[i]:
                        return i
                print("Value Not Found.")
                return -1

        def traverse(self):
            if self.size == 0:
                print("Stack Underflow")
            else:
                print(end="Front - ")
                for i in range(self.size):
                    print(self.queue[i], end=" - ")
                print("Rear")

    q = Queue()
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.traverse()
    print(q.DeQueue())
    print(q.search(2))
    q.traverse()

def QueueLinkedList():
    class Node:
        def __init__(self, data=None):
            self.data, self.next = data, None

    class Queue:
        def __init__(self):
            self.size = 0
            self.front = None
            self.rear = None

        def EnQueue(self, data):
            New = Node(data)
            if self.rear and self.front is not None:
                self.rear.next = New
                self.rear = New
                self.size += 1
            else:
                self.rear = self.front = New
                self.size += 1

        def DeQueue(self):
            if self.rear and self.front is not None:
                front = self.front.data
                self.front = self.front.next
                self.size -= 1
                return front
            else:
                print("Queue Underflow")
                return -1

        def size(self):
            return self.size

        def search(self, data):
            if self.rear and self.front is None:
                print("Queue Underflow")
            else:
                temp = self.front
                i = 0
                while temp is not None:
                    i += 1
                    if data == temp.data:
                        return i
                    temp = temp.next
                print("Value Not Found.")
                return -1

        def traverse(self):
            if self.rear and self.front is None:
                print("Queue Underflow")
            else:
                temp = self.front
                print(end="Front <- ")
                while temp is not None:
                    print(temp.data, end=" <- ")
                    temp = temp.next
                print("Rear")


    q = Queue()
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)
    q.traverse()
    print(q.DeQueue())
    q.EnQueue(4)
    print(q.search(2))
    q.traverse()


# QueueArray()
# QueueLinkedList()
