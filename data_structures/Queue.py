from Node import Node

class Queue():
    # FIFO

    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,key):
        if self.head==None:
            self.head=Node(key)
            self.tail=self.head
        else:
            self.tail.next=Node(key)
            self.tail=self.tail.next
    
    def dequeue(self):
        head=self.head
        assert head is not None, "Queue is empty. Nothing to dequeue."
        self.head=head.next
        return head.key

"""
x=Queue()
print(x.head)
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
print(x.head.key)
print(x.dequeue())
print(x.dequeue())
print(x.dequeue())
#print(x.dequeue())
"""

