# Python3 program to print Bottom 
# View of Binary Tree 
   
# Tree node class 
class Node: 
      
    def __init__(self, key): 
          
        self.data = key 
        self.hd = 1000000
        self.left = None
        self.right = None
   
# Method that prints the bottom view. 
def bottomView(root): 
  
    if (root == None): 
        return
      
    # Initialize a variable 'hd' with 0 
    # for the root element. 
    hd = 0
      
    # TreeMap which stores key value pair 
    # sorted on key value 
    m = dict() 
   
    # Queue to store tree nodes in level 
    # order traversal 
    q = [] 
   
    # Assign initialized horizontal distance 
    # value to root node and add it to the queue. 
    root.hd = hd 
      
    # In STL, append() is used enqueue an item 
    q.append(root)   
   
    # Loop until the queue is empty (standard 
    # level order loop) 
    while (len(q) != 0): 
        temp = q[0] 
          
        # In STL, pop() is used dequeue an item 
        q.pop(0)   
          
        # Extract the horizontal distance value 
        # from the dequeued tree node. 
        hd = temp.hd 
   
        # Put the dequeued tree node to TreeMap 
        # having key as horizontal distance. Every 
        # time we find a node having same horizontal 
        # distance we need to replace the data in 
        # the map. 
        m[hd] = temp.data 
   
        # If the dequeued node has a left child, add 
        # it to the queue with a horizontal distance hd-1. 
        if (temp.left != None): 
            temp.left.hd = hd - 1
            q.append(temp.left) 
   
        # If the dequeued node has a right child, add 
        # it to the queue with a horizontal distance 
        # hd+1. 
        if (temp.right != None): 
            temp.right.hd = hd + 1
            q.append(temp.right) 
   
    # Traverse the map elements using the iterator. 
    for i in sorted(m.keys()): 
        print(m[i], end = ' ') 
          
# Driver Code 
if __name__=='__main__': 
      
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(5) 
    root.left.right = Node(3) 
    root.right.left = Node(4) 
    root.right.right = Node(25) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14) 
      
    print("Bottom view of the given binary tree :") 
      
    bottomView(root) 
