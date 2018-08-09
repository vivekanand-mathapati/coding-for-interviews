class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_to_end(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data, prev=self.tail)
            self.tail = self.tail.next
    
    def append_to_front(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head.prev = Node(data, next=self.head)
            self.head = self.head.prev

    def find_element(self, data):
        if self.head.data == data:
            print(data, 'Found in the list')
            return
        elif self.tail.data == data:
            print(data, 'Found in the list')
            return
        else:
            curr = self.head.next
            while curr is not self.tail:
                if curr.data == data:
                    print(data, 'Found in the list')
                    return
                curr = curr.next
            print(data, 'Not found in the list')
            return

    def delete(self, data):
        if self.head.data == data:
            print(data, 'Is deleted from the list')
            self.head = self.head.next
            return
        elif self.tail.data == data:
            print(data, 'Is deleted from the list')
            self.tail = self.tail.prev
            return 
        else: 
            curr = self.head
            while curr is not self.tail:
                if curr.next.data == data:
                    print(data, 'deleted from the list')
                    curr.next = curr.next.next
                    return
                curr = curr.next
            print(data, 'Is not present in the list')
            return

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def display_reverse(self):
        curr = self.tail
        while curr:
            print(curr.data)
            curr = curr.prev

obj = DoublyLinkedList()
obj.append_to_end(30)
obj.append_to_end(40)
obj.append_to_end(50)
obj.append_to_end(60)

obj.append_to_front(20)
obj.append_to_front(10)

print('display elements')
obj.display()
print('reverse display')
obj.display_reverse()

obj.find_element(10)
obj.find_element(90)

obj.delete(20)
print('display elements')
obj.display()