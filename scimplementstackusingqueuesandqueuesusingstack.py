# Program to implement a stack using  
# two queue  
from queue import Queue 
  
class Stack: 
      
    def __init__(self): 
          
        # Two inbuilt queues  
        self.q1 = Queue() 
        self.q2 = Queue()  
              
        # To maintain current number  
        # of elements 
        self.curr_size = 0
  
    def push(self, x): 
        self.curr_size += 1
  
        # Push x first in empty q2  
        self.q2.put(x)  
  
        # Push all the remaining  
        # elements in q1 to q2.  
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        # swap the names of two queues  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q 
  
    def pop(self): 
  
        # if no elements are there in q1  
        if (self.q1.empty()):  
            return
        self.q1.get()  
        self.curr_size -= 1
  
    def top(self): 
        if (self.q1.empty()): 
            return -1
        return self.q1.queue[0] 
  
    def size(self): 
        return self.curr_size 
  
#

#pop effective

from collections import deque
 
 
# Implement stack using two queues
class Stack:
 
    # Constructor
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def add(self, data):
        # Push the given item into the first queue
        self.q1.append(data)
 
    # Remove the top item from the stack
    def poll(self):
 
        # if the first queue is empty
        if not self.q1:
            print("Stack Underflow!!")
            exit(0)
 
        # Move all elements except last from the first queue to the second queue
        front = None
        while self.q1:
 
            if len(self.q1) == 1:
                front = self.q1.popleft()
            else:
                self.q2.append(self.q1.popleft())
 
        # Return the last element after moving all elements back to the first queue.
        while self.q2:
            self.q1.append(self.q2.popleft())
 
        return front
 
 
if __name__ == '__main__':
 
    keys = 1, 2, 3, 4, 5
 
    # insert the above keys into the stack
    s = Stack()
 
    for key in keys:
        s.add(key)
 
    while s:
        print(s.poll())
 
    print(s.poll())


#queue using stack
    
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
from collections import deque
 
 
# Implement a queue using two stacks
class Queue:
 
    # Constructor
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
 
    # Add an item to the queue
    def enqueue(self, data):
 
        # Move all elements from the first stack to the second stack
        while len(self.s1):
            self.s2.append(self.s1.pop())
 
        # push item into the first stack
        self.s1.append(data)
 
        # Move all elements back to the first stack from the second stack
        while len(self.s2):
            self.s1.append(self.s2.pop())
 
    # Remove an item from the queue
    def dequeue(self):
 
        # if the first stack is empty
        if not self.s1:
            print("Underflow!!")
            exit(0)
 
        # return the top item from the first stack
        return self.s1.pop()
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    # insert above keys
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())        # 1
    print(q.dequeue())  
 

from collections import deque
 
 
# Implement a queue using two stacks
class Queue:
 
    # Constructor
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
 
    # Add an item to the queue
    def enqueue(self, data):
        # push item into the first stack
        self.s1.append(data)
 
    # Remove an item from the queue
    def dequeue(self):
        # if both stacks are empty
        if not self.s1 and not self.s2:
            print("Underflow!!")
            exit(0)
 
        # if the second stack is empty, move elements from the first stack to it
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
 
        # return the top item from the second stack
        return self.s2.pop()
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    # insert above keys
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())    # 1
    print(q.dequeue())    # 2
 
