
# Given the head of a linked list, rotate the list to the right by k places.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head==None or head.next==None or k==0:
            return head

        # Note that rotating k times is the same as rotating k % length(list) times.
        # Thus, we first determine the length of the list to cover cases when k is huge.
        # We can return the original list in case k % length(list) == 0. 
        # Otherwise, we temporarily turn the list into a circle to increase the efficiency of the algorithm. 
        # Instead of looping over k % length(list) rotations by 1 place we can then follow the list a fixed number of times and reroute the head and de-link the end node.
        
        # get the length of the list and go to the last node.
        curr=head
        len_list=1
        while curr.next!=None:
            curr=curr.next
            len_list+=1
        k_small = k % len_list
        if k_small==0: # in this case we can return the original list. 
            return head
        curr.next=head # turns the list into a circle.

        # next we follow the deformed list from the beginning a fixed number of steps.
        curr=head
        for i in range(2*len_list - k_small-1):
            curr=curr.next
            if i==len_list-k_small-1: # now we are at the new head after rotating by k places.
                head=curr
        curr.next=None # de-lin the end node.

        return head