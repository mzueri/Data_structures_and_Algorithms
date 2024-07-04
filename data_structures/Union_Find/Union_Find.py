
# Union-Find data structure

class Union_Find():

    def __init__(self,*elements):
        self.dic={} # this dictionary stores the parent of each set element. 
        for element in elements: # if elements are given, then initialize each element as a new set of size 1. 
            self.makeNewSet(element)

    def makeNewSet(self,x): # Add new data element x. x will be a new set of size 1.
        assert x not in list(self.dic.keys()), f"The element \'{str(x)}\' already exists."
        self.dic[x]=[x,0] # x is root of itself. We use a list (tuples are immutable) to also store the height of the subtree rooting at x. 
        # This is necessary for the union method to concat the tree of smaller hight to the tree of greater height. 
        # -> Performance guarantee.

    def find(self,x): # Return the representation of the set x belongs to.
        if x not in list(self.dic.keys()):
            print(f"There is no \'{str(x)}\'")
            return None 
        visited_nodes=[] # we store the visited nodes to get up to the root for path compression.
        while self.dic[x][0]!=x:
            visited_nodes.append(x)
            x=self.dic[x][0]
        root=x # now x is the root.
        for node in visited_nodes:
            self.dic[node]=[root,0] # path compression.
            self.dic[root]=[root,1]
        return root

    def union(self,r,s): # Union of the two sets which r and s lie in.
        assert r in list(self.dic.keys()), f"The element \'{str(r)}\' does not exist yet."
        assert s in list(self.dic.keys()), f"The element \'{str(s)}\' does not exist yet."
        root_r,height_r=self.dic[self.find(r)]
        root_s,height_s=self.dic[self.find(s)]
        if root_r==root_s:
            print(f"\'{str(r)}\' and \'{str(s)}\' are already in the same set.")
        else:
            if height_r>height_s:
                self.dic[root_s][0]=root_r
            elif height_r==height_s: # in this case we choose the tree rooting at s to become a subtree of the tree rooting at r. 
                self.dic[root_s][0]=root_r
                self.dic[root_r][1]+=1
            else:
                self.dic[root_r][0]=root_s


"""
uf=Union_Find("m","e","l","v","i","n")
print(uf.dic)
uf.union("m","l")
print(uf.dic)
uf.union("m","l")
print(uf.dic)
uf.union("l","e")
print(uf.dic)
uf.union("i","n")
print(uf.dic)
uf.union("e","n")
print(uf.dic)
# illustration of path compression.
uf.find("n")
print(uf.dic)
"""