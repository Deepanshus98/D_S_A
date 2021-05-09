# Recursive function to perform preorder traversal on the tree
def preorder(root):
 
    # return if the current node is empty
    if root is None:
        return
 
    # Display the data part of the root (or current node)
    print(root.data, end=' ')
 
    # Traverse the left subtree
    preorder(root.left)
 
    # Traverse the right subtree
    preorder(root.right)



# Iterative function to perform preorder traversal on the tree
def preorderIterative(root):
 
    # return if the tree is empty
    if root is None:
        return
 
    # create an empty stack and push the root node
    stack = deque()
    stack.append(root)
 
    # loop till stack is empty
    while stack:
 
        # pop a node from the stack and print it
        curr = stack.pop()
 
        print(curr.data, end=' ')
 
        # push the right child of the popped node into the stack
        if curr.right:
            stack.append(curr.right)
 
        # push the left child of the popped node into the stack
        if curr.left:
            stack.append(curr.left)
 
    # the right child must be pushed first so that the left child
    # is processed first (FIFO order
