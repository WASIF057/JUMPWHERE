class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def arr_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.key != root2.key:
        return False
    else:
        return arr_symmetric(root1.left, root2.right) and arr_symmetric(root1.right, root2.left)
        
def is_symmetric(root):
    if root is None:
        return True
    return arr_symmetric(root.left, root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(is_symmetric(root))
