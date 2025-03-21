# Given a list of elements. 
# If this list was turned into a set, return the powerset of this set as a list. 
# The order of the elements does not matter. 

# the following function is only for testing.
def get_unique_sublists(list: list) -> list:
    unique_sublists=[]
    for sublist in list:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists

def powerset(list: list) -> list:
    # the idea is to use depth first search on a binary tree with root []. 
    # At each height we decide to add a particular element or not. 
    # curr will be extended until a leaf is reached. Then we go back the stack in DFS, i.e. we backtrack. 

    res,curr = [],[] 

    def backtrack(index):
        if index==len(list):
            res.append(curr[:]) # use a shallow copy of curr!
            return

        backtrack(index+1) # do not consider list[index]

        curr.append(list[index]) # do consider list[index], thus, add it. 
        backtrack(index+1)
        curr.pop() # remove the added element again to go back.  

    backtrack(0)

    # Testing the output
    assert len(res)==2**len(list), "Not the right number of subsets. Something went wrong."
    assert len(res)==len(get_unique_sublists(res)), "Not distinct elements in the output. Fix."
    assert list in res, "list is not in the output. Fix."
    assert [] in res, "[] is not in the subset. Fix."
    
    return res

#print(powerset([1,2,3]))
#print(powerset([1,2,3,4]))
