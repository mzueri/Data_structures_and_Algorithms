
import math

class ab_TreeNode():
    def __init__(self,leaf,keys):
        assert isinstance(leaf,bool), "Parameter leaf should be boolean."
        if leaf:
            assert isinstance(keys,int), "Leafs can only have 1 integer key."
            self.keys=keys
            self.parent=None
            self.children=[]
        else:
            assert isinstance(keys,list), "Parameter keys should be given as a list for internal nodes."
            self.keys=sorted([-float("inf"),float("inf")]+keys)
            self.parent=None
            self.children=[]
    


# The following implements an (a,b)-tree

class ab_Tree():

    def __init__(self,a:int,b:int,childkey1:float,childkey2:float):
        assert isinstance(a,int) & isinstance(b,int),"a,b must be integers."
        assert a>=2 and b>=2*a-1, "(a,b) does not fulfill the necessary requirements."
        assert isinstance(childkey1,float) & isinstance(childkey2,float) & childkey1!=childkey2,"Make sure the keys of the two initialized child nodes are distinct numbers."
        self.a=a
        self.b=b
        self.root=ab_TreeNode(leaf=False,keys=[min(childkey1,childkey2)])
        child1=ab_TreeNode(leaf=True,keys=childkey1)
        child2=ab_TreeNode(leaf=True,keys=childkey2)
        self.root.children=[child1,child2]
        child1.parent=self.root
        child2.parent=self.root

    def isleaf(self,v):
        if v.children==[]:
            return True
        else:
            return False
        
    def find(self,key:int,approx=False):
        v=self.root
        while v!=None and not self.isleaf(v): # go to the leaf node whose keys-element is the smallest element greater than key.
            i=min([j for j in list(range(len(v.keys)-1)) if (key>v.keys[j] and key<=v.keys[j+1])])
            parent=v
            v=v.children[i]
            v.parent=parent
        if approx:
            assert v.keys!=key, "This key already exists."
            insert_left=True
            if v.keys>key:
                return v,insert_left
            else:
                return v,not insert_left
        if v.keys==key:
            return v
        return None

    def insert(self,key):
        w,insert_left=self.find(key,approx=True)
        v=w.parent        
        if insert_left:
            v.children=v.children[:v.children.index(w)]+[ab_TreeNode(leaf=True,keys=key)]+v.children[v.children.index(w):]
            v.keys.append(key)
            v.keys.sort()
        else:
            v.children=v.children[:v.children.index(w)+1]+[ab_TreeNode(leaf=True,keys=key)]+v.children[v.children.index(w)+1:]
            v.keys.append(w.keys)  
            v.keys.sort()
        # check if the condition of a a-b Tree is fulfilled. If the number of children is > b, then rebalance. 
        if len(v.children)>self.b:
            while len(v.children)>self.b:
                if v!=self.root:
                    u=v.parent
                else:
                    u=self.root
                # we now divide v into two children from u: v1 and v2. 
                cut=math.ceil((self.b+1)/2)
                v1=ab_TreeNode(leaf=False,keys=v.keys[1:cut])
                v1.children=v.children[:cut]
                v2=ab_TreeNode(leaf=False,keys=v.keys[cut+1:-1])
                v2.children=v.children[cut:]
                if u==v.parent:
                    u.children=u.children[:u.children.index(v)]+[v1,v2]+u.children[u.children.index(v)+1:]
                    u.keys.append(v.keys[cut])
                    u.keys.sort()
                else:
                    u.children=[v1,v2]
                    u.keys=[-float("inf"),v.keys[cut],float("inf")]
                for vi in u.children:
                    vi.parent=u
                for child in v1.children:
                    child.parent=v1
                for child in v2.children:
                    child.parent=v2
                v=u
        return None

"""
t=ab_Tree(2,3,0,1)
#for i in range(2,15):
for i in range(14,1,-1):
    t.insert(i)
    v=t.root
    print("keys root: ")
    print(v.keys)
    print("keys children: ")
    for child in v.children:
        print(child.keys)
    if not any([t.isleaf(child) for child in v.children]):
        print("keys grandchildren: ")
        for child in v.children:
            for grandchild in child.children:
                print(grandchild.keys)
            print()
    if not any([t.isleaf(grandchild) for child in v.children for grandchild in child.children]):
        print("keys grandgrandchildren: ")
        for child in v.children:
            for grandchild in child.children:
                for grandgrandchild in grandchild.children:
                    print(grandgrandchild.keys)
                print()          
    print()
    """
