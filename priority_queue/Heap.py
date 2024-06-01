
# The following implements a (max) Heap.
# binary tree with priority queue structure. Implementation with an array.

class Heap(): 

    def __init__(self,list=[]):
        self.list=[]
        for item in list: # this takes time O(n)
            self.insert(item) 
    
    def swap(self,index_child,index_parent): # swap parent with child
        tmp=self.list[index_child]
        self.list[index_child]=self.list[index_parent]
        self.list[index_parent]=tmp

    def swim_up(self,index_child:int):
        while (self.list[index_child]>self.list[max(0,int((index_child+1)/2)-1)]): # key of child is greater than key of parent. -> Swim it up the binary tree.
            index_parent=max(0,int((index_child+1)/2)-1) # Lemma starts counting indices at 1.
            self.swap(index_child,index_parent)
            index_child=index_parent

    def insert(self,key:int): # TODO: change int to Node
        self.list.append(key)
        self.swim_up(len(self.list)-1)

    def get_indices_children(self,index_parent):
        if 2*(index_parent+1)>len(self.list):
            return []
        elif 2*(index_parent+1)==len(self.list):
            return [2*(index_parent+1)-1]
        else:
            return [2*(index_parent+1)-1,2*(index_parent+1)]

    def sink_down(self,index_parent:int):
        indices_children=self.get_indices_children(index_parent)
        while indices_children!=[]: # while the parent node has children.
            if all([self.list[index_parent]>self.list[index] for index in indices_children]):
                # priority queue structure is preserved. Done.
                break
            elif len(indices_children)==1:
                index_child=indices_children[0]
            elif self.list[indices_children[0]]>self.list[indices_children[1]]:
                index_child=indices_children[0]
            else:
                index_child=indices_children[1]
            self.swap(index_child,index_parent)
            index_parent=index_child
            indices_children=self.get_indices_children(index_parent)
            
    def dequeue_max(self):
        assert len(self.list)>=1, "Dequeue_max not possible on empy heap."
        max=self.list[0]
        self.list[0]=self.list[len(self.list)-1]
        self.list=self.list[:-1]
        self.sink_down(0)
        return max
            

"""
l=[3,2,10,8,7,22,4,5,9,11,1,15,100,19]
x=Heap()
for item in l:
    x.insert(item)
print(x.list)
y=Heap(l)
assert x.list==y.list, "Heap construction failed."
print("Start to dequeue_max.")
while len(y.list)>0:
    print(y.dequeue_max())
    print(y.list)
"""