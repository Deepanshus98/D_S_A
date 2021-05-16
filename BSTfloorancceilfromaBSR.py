# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Recursive function to find the floor and ceil of a given key in a BST
def findFloorCeil(root, floor, ceil, key):
 
    while root:
        # if a node with the desired value is found, both floor and ceil is equal
        # to the current node
        if root.data == key:
            floor = ceil = root
            break
 
        # if the given key is less than the root node, visit the left subtree
        elif key < root.data:
            # update ceil to the current node before visiting the left subtree
            ceil = root
            root = root.left
 
        # if the given key is more than the root node, visit the right subtree
        else:
            # update floor to the current node before visiting the right subtree
            floor = root
            root = root.right
 
    return floor, ceil
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               8
             /   \
            /     \
           4       10
          / \     /  \
         /   \   /    \
        2     6 9     12
    '''
 
    keys = [2, 4, 6, 8, 9, 10, 12]
 
    root = None
    for key in keys:
        root = insert(root, key)
 
    # find the ceil and floor for each key
    for i in range(15):
 
        floor, ceil = findFloorCeil(root, None, None, i)
 
        print(i, end=' —> ')
        print("Floor is", floor.data if floor else None, end=' and ')
        print("Ceil is", ceil.data if ceil else None)
