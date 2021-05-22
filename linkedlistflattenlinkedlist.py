# A Linked List Node
class Node:
    def __init__(self, data, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down
 
 
# Takes two lists sorted in increasing order and merge their nodes
# to make one big sorted list, which is returned
def sortedMerge(a, b):
 
    if a is None:
        return b
 
    elif b is None:
        return a
 
    # pick either `a` or `b`, and recur
    if a.data <= b.data:
 
        result = a
        result.down = sortedMerge(a.down, b)
 
    else:
 
        result = b
        result.down = sortedMerge(a, b.down)
 
    return result
 
 
'''
    Split the given list's nodes into front and back halves.
    If the length is odd, the extra node should go in the front list.
    It uses the fast/slow reference strategy.
'''
 
 
def frontBackSplit(source):
 
    # if the length is less than 2, handle it separately
    if source is None or source.down is None:
        return source, None
 
    (slow, fast) = (source, source.down)
 
    # advance `fast` two nodes, and advance `slow` one node
    while fast:
        fast = fast.down
        if fast:
            slow = slow.down
            fast = fast.down
 
    # `slow` is before the midpoint of the list, so split it in two
    # at that point.
    A = (source, slow.down)
    slow.down = None
 
    return A
 
 
# Sort a given linked list using the merge sort algorithm
def mergesort(head):
 
    # base case — length 0 or 1
    if head is None or head.down is None:
        return head
 
    # split `head` into `a` and `b` sublists
    front, back = frontBackSplit(head)
 
    # recursively sort the sublists
    front = mergesort(front)
    back = mergesort(back)
 
    # answer = merge the two sorted lists
    return sortedMerge(front, back)
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.down
    print("None")
 
 
# Iterative function to flatten and sort a given list
def flatten(head):
 
    curr = head
    while curr:
        temp = curr
        while temp.down:
            temp = temp.down
        temp.down = curr.next
        curr = curr.next
 
 
# Helper function to build a linked list from elements of a given list
def createVerticalList(head, A):
 
    for key in A:
        head = Node(key, head)
    return head
 
 
if __name__ == '__main__':
 
    first = [8, 6, 4, 1]
    second = [7, 3, 2]
    third = [9, 5]
    fourth = [12, 11, 10]
 
    head = createVerticalList(None, first)
    head.next = createVerticalList(head.next, second)
    head.next.next = createVerticalList(head.next.next, third)
    head.next.next.next = createVerticalList(head.next.next.next, fourth)
 
    # flatten the list
    flatten(head)
 
    # sort the list
    mergesort(head)
 
    # print the flattened and sorted linked list
    printList(head)
