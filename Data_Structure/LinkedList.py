def SinglyLinkedList():
    class Node:
        def __init__(self, data=None):
            self.data, self.next = data, None

    class SingleLL:
        def __init__(self):
            self.head, self.size = None, 0

        def addFirst(self, data):
            New = Node(data)
            New.next = self.head
            self.head = New
            self.size += 1

        def addLast(self, data):
            temp, New = self.head, Node(data)
            if temp is not None:
                while temp.next is not None:
                    temp = temp.next
                temp.next = New
                self.size += 1
            else:
                self.head = New

        def addBefore(self, before, data):
            temp, New = self.head, Node(data)
            while temp is not None:
                if before == temp.next.data:
                    New.next = temp.next
                    temp.next = New
                    self.size += 1
                    return
                temp = temp.next
            print("Can't add before an item which is not present.")

        def addAfter(self, after, data):
            temp, New = self.head, Node(data)
            while temp is not None:
                if after == temp.data:
                    New.next = temp.next
                    temp.next = New
                    self.size += 1
                    return
                temp = temp.next
            print("Can't add after an item which is not present.")

        def replace(self, posi, data):
            temp = self.head
            i = 1
            while temp is not None:
                if posi == i:
                    temp.data = data
                    return
                temp = temp.next
                i += 1

            print("Can't add\n", "Max Size:", i)

        def remove(self, data):
            temp = self.head
            if temp.data == data:
                self.head = self.head.next
                self.size -= 1
                print("Delete Successful.")
                return
            while temp is not None:
                if data == temp.next.data:
                    temp.next = temp.next.next
                    self.size -= 1
                    print("Delete Successful.")
                    return
                temp = temp.next
            print("Can't delete.\nData value not present.")

        def traverse(self):
            temp = self.head
            if self.head is None:
                print("List is empty")
                return
            print(f"Singly Linked List({self.size}):")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

        def searchData(self, data):
            temp = self.head
            i = 1
            if temp.data == data:
                print("Before: None")
                print("After:", temp.next.data)
                print("Index:", i)
                return

            while temp is not None:
                i += 1
                if data == temp.next.data:
                    print("Before:", temp.data)
                    try:
                        print("After:", temp.next.next.data)
                    except:
                        print("After: None")
                    print("Index:", i)
                    return
                temp = temp.next

            print("Can't add before an item which is not present.")

    sll = SingleLL()
    sll.addLast(input("Enter Data Value: "))
    sll.addLast(input("Enter Data Value: "))
    sll.addLast(input("Enter Data Value: "))
    sll.addAfter(input("Enter value of data after which you want to add: "), input("Enter Data Value: "))
    sll.addBefore(input("Enter value of data before which you want to add: "), input("Enter Data Value: "))
    sll.replace(int(input("Enter Position: ")), input("Enter Data Value: "))
    sll.traverse()
    sll.remove(input("Enter Value to Delete: "))
    sll.traverse()
    sll.searchData(input("Enter Search Value: "))


def DoubllyLinkedList():
    class Node:
        def __init__(self, data=None):
            self.left, self.data, self.right = None, data, None

    class DoubllyLL:
        def __init__(self):
            self.head, self.tail, self.size = None, None, 0

        def addFirst(self, data):
            New = Node(data)
            if self.tail and self.head is not None:
                self.head.left = New
                New.right = self.head
                self.head = New
                self.size += 1
            else:
                self.tail = self.head = New

        def addLast(self, data):
            New = Node(data)
            if self.tail and self.head is not None:
                self.tail.right = New
                New.left = self.tail
                self.tail = New
                self.size += 1
            else:
                self.tail = self.head = New
                self.size += 1


        def addBefore(self, before, data):
            temp, New = self.tail, Node(data)
            while temp is not None:
                if before == temp.data:
                    try:
                        New.left, temp.left.right = temp.left, New
                        temp.left, New.right = New, temp
                        self.size += 1
                    except:
                        self.addFirst(data)
                    return
                temp = temp.left
            print("Can't add before an item which is not present.")

        def addAfter(self, after, data):
            temp, New = self.head, Node(data)
            while temp is not None:
                if after == temp.data:
                    try:
                        New.right, temp.right.left = temp.right, New
                        New.left, temp.right = temp, New
                        self.size += 1
                    except:
                        self.addLast(data)
                    return
                temp = temp.right
            print("Can't add after an item which is not present.")

        def replace(self, posi, data):
            temp = self.head
            i = 1
            while temp is not None:
                if posi == i:
                    temp.data = data
                    return
                temp = temp.right
                i += 1

            print("Can't add\n", "Max Size:", i)

        def remove(self, data):
            temp = self.head
            if self.head.data == data:
                self.head = self.head.right
                self.head.left = None
                self.size -= 1
                print("Delete Successful.")
            elif self.tail.data == data:
                self.tail = self.tail.left
                self.head.right = None
                self.size -= 1
                print("Delete Successful.")
            else:
                while temp is not None:
                    if data == temp.data:
                        temp.left.right, temp.right.left = temp.right, temp.left
                        print("Delete Successful.")
                        self.size -= 1
                        return
                    temp = temp.right
                print("Can't delete.\nData value not present.")

        def traverseRigth(self):
            temp = self.head
            if self.head is None:
                print("List is empty")
                return
            print(f"Doublly Linked List({self.size}) HEAD->TAIL:")
            print(end="HEAD <-> ")
            while temp is not None:
                print(temp.data, end=" <-> ")
                temp = temp.right
            print("TAIL")

        def traverseLeft(self):
            temp = self.tail
            if self.tail is None:
                print("List is empty")
                return
            print(f"Doublly Linked List({self.size}) TAIL->HEAD:")
            print(end="TAIL <-> ")
            while temp is not None:
                print(temp.data, end=" <-> ")
                temp = temp.left
            print("HEAD")

        def searchData(self, data):
            temp, li, ri = self.head, 1, self.size
            if self.head.data == data:
                print("Before: None")
                print("After:", self.head.right.data)
                print("Left-Index:", 1)
                print("Right-Index:", self.size)
            elif self.tail.data == data:
                print("Before:", self.tail.left.data)
                print("After: None")
                print("Left-Index:", self.size)
                print("Right-Index:", 1)
            else:
                while temp is not None:
                    if data == temp.data:
                        print("Before:", temp.left.data)
                        print("After:", temp.right.data)
                        print("Left-Index:", li)
                        print("Right-Index:", ri)
                        return
                    temp = temp.right
                    li += 1
                    ri -= 1

                print("Can't add before an item which is not present.")

    dll = DoubllyLL(Node(input("Enter Data Value: ")))
    dll.addLast(input("Enter Data Value: "))
    dll.addFirst(input("Enter Data Value: "))
    dll.addAfter(input("Enter value of data after which you want to add: "), input("Enter Data Value: "))
    dll.addBefore(input("Enter value of data before which you want to add: "), input("Enter Data Value: "))
    dll.traverseRigth()
    dll.replace(int(input("Enter Position: ")), input("Enter Data Value: "))
    dll.remove(input("Enter Value to Delete: "))
    dll.traverseLeft()
    dll.searchData(input("Enter Search Value: "))

def CircularLinkedList():
    class Node:
        def __init__(self, data=None):
            self.data, self.next = data, None

    class CircularLL:
        def __init__(self):
            self.head, self.tail, self.maxSize, self.size = None, None, 5, 0

        def addFirst(self, data):
            New = Node(data)
            if self.tail and self.head is not None:
                self.tail.next = New
                New.next = self.head
                self.head = New
                self.size += 1
            else:
                self.tail = self.head = New
                New.next = self.head

        def addLast(self, data):
            New = Node(data)
            if self.tail and self.head is not None:
                self.tail.next = New
                self.tail = New
                self.tail.next = self.head
                self.size += 1
            else:
                self.tail = self.head = New
                New.next = self.head

        def addBefore(self, before, data):
            temp, New = self.head, Node(data)
            if before == temp.data:
                New.next = self.head
                self.head = New
                self.tail.next = self.head
                self.size += 1
            else:
                while temp.next != self.head:
                    if before == temp.next.data:
                        New.next = temp.next
                        temp.next = New
                        self.size += 1
                        return
                    temp = temp.next
                print("Can't add before an item which is not present.")

        def addAfter(self, after, data):
            temp, New = self.head, Node(data)
            if after == temp.data:
                New.next = temp.next
                temp.next = New
                self.size += 1
            else:
                while temp.next != self.head:
                    if after == temp.data:
                        New.next = temp.next
                        temp.next = New
                        self.size += 1
                        return
                    temp = temp.next
                print("Can't add after an item which is not present.")

        def remove(self, data):
            temp = self.head
            if temp.data == data:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.size -= 1
                print("Delete Successful.")
            else:
                while temp.next != self.head:
                    if data == temp.next.data:
                        temp.next = temp.next.next
                        self.size -= 1
                        print("Delete Successful.")
                        return
                    temp = temp.next
                print("Can't delete.\nData value not present.")

        def traverse(self):
            temp = self.head
            if self.head is None:
                print("List is empty")
            else:
                print(f"Circular Linked List({self.size}):")
                print("HEAD ->", temp.data, end=" -> ")
                while temp.next != self.head:
                    temp = temp.next
                    print(temp.data, end=" -> ")
                print("HEAD")

        def searchData(self, data):
            pass

    cll = CircularLL()
    cll.addLast(input("Enter Data Value: "))
    cll.addAfter(input("Enter value of data after which you want to add: "), input("Enter Data Value: "))
    cll.traverse()
    cll.addBefore(input("Enter value of data before which you want to add: "), input("Enter Data Value: "))
    cll.traverse()
    # cll.replace(int(input("Enter Position: ")), input("Enter Data Value: "))
    cll.remove(input("Enter Value to Delete: "))
    cll.traverse()
    # cll.searchData(input("Enter Search Value: "))

# SinglyLinkedList()
# DoubllyLinkedList()
# CircularLinkedList()
