
from Node import Node

class Stack():
    
    def __init__(self):
        self.head=None

    def push(self,key):
        if self.head==None:
            self.head=Node(key)
        else:
            old_head=self.head
            self.head=Node(key)
            self.head.next=old_head
        
    def pop(self):
        assert self.head is not None, "Stack is empty. Nothing to pop."
        head=self.head
        self.head=self.head.next
        return head.key

"""
s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.head.key)
print()
print(s.pop())
print(s.pop())
print(s.pop())
#print(s.pop())
"""