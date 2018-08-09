class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data, None)  
            self.tail = self.head          
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            print(data, 'Is deleted from list')
        else:
            curr = self.head.next
            is_deleted = False
            while curr:
                if curr.next.data == data and curr.next.next != None:
                    is_deleted = True
                    curr.next = curr.next.next
                    break
                elif curr.next.data == data and curr.next.next == None:
                    is_deleted = True
                    curr.next = None
                    break
                else:
                    curr = curr.next
            if is_deleted:
                print(data, 'Is deleted from list')
            else:
                print(data, 'Is not found in the list')

obj = LinkedList()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)
obj.append(60)

obj.display()

obj.delete(10)
obj.delete(20)
# obj.delete(70)

obj.display()