
from Node import Node

class Linked_list():
    def __init__(self,array):
        assert type(array) is list, "Initialize linked list with a list object."
        if len(array)==0:
            self.head=None
            self.tail=None
        else:
            current=Node(array[0])
            self.head=current
            i = 1
            while i < len(array):
                next=Node(array[i])
                current.next=next
                current=next
                i+=1
            self.tail=current

"""
ll2=Linked_list([])
print(ll2.head)
ll=Linked_list([1,2,3,4])
print(ll.head.key)
print(ll.head.next.key)
print(ll.head.next.next.key)
print(ll.head.next.next.next.key)
print(ll.tail.key)
"""