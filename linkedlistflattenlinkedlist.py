#This question can be solved by Depth First Search. It is similar with question 114. Flatten Binary Tree to Linked List. The difference is using doubly linked list this time.

#Start traversing the double linked list. Once meet a node with child, we first store the current node’s next node. Then we connect the current node to child node and traversal child node. After done traversing child node, we want to connet the tail of child node to the original current node’s next node. We can use dfs to recursivly connect the child node and even child’s child node.

#As this is doubly linked list, do not forget the prev pointer.

#Code
def flattenChild(node):
            if node.next is None: return node
            while node and node.next:
                if node.child:
                    tmp = node.next
                    node.next, node.child.prev= node.child, node
                    node.child = None
                    node = flattenChild(node.next)
                    node.next, tmp.prev= tmp, node
                node = node.next
            return node
                
        node = head
        while node:
            if node.child:
                tmp = node.next
                node.next, node.child.prev= node.child, node
                node.child = None
                node = flattenChild(node.next)
                if tmp:
                    node.next, tmp.prev= tmp, node
            else:
                node = node.next
        return head
