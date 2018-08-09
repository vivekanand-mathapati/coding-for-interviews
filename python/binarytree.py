class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = Node()

def insert_node(data):
    root = insert(root, data)

def insert(root, data):
    if root is None:
        root = Node(data)
        return root
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def display():
    in_order(root)

def in_order(root):
    if root is None:
        in_order(root.left)
        print(root.data)
        in_order(root.right)


# obj = BinarySearchTree()
# obj.insert_node(10)
# obj.insert_node(5)
# obj.insert_node(20)
# obj.display()
insert_node(10)
insert_node(5)
insert_node(20)
display()