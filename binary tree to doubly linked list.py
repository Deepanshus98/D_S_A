# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to print a given doubly linked list
def printDLL(head):
 
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.right
 
 
# Function to in-place convert a given binary tree into a doubly linked list
# by doing normal inorder traversal
def convert(root, head):
 
    # base case: tree is empty
    if root is None:
        return head
 
    # recursively convert the left subtree first
    head = convert(root.left, head)
 
    # store right child
    right = root.right
 
    # insert the current node at the beginning of a doubly linked list
    root.right = head
    if head:
        head.left = root
 
    head = root
 
    # recursively convert the right subtree
    return convert(right, head)
 
 
# Function to reverse a doubly-linked list
def reverse(head):
 
    prev = None
    current = head
 
    while current:
        # swap current.left with current.right
        temp = current.left
        current.left = current.right
        current.right = temp
 
        prev = current
        current = current.left
 
    return prev
 
 
# The main function to in-place convert a given binary tree into a
# doubly linked list
def convertBinaryTreeToDDL(root):
 
    # head of the doubly linked list
    head = None
 
    # convert the above binary tree into doubly linked list
    head = convert(root, head)
 
    # reverse the linked list
    head = reverse(head)
 
    # print the list
    printDLL(head)
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    convertBinaryTreeToDDL(root)
