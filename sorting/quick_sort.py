
# at the beginning we assume that the array entries are randomly allocated. 

def quick_sort(l:list)->list:
    assert type(l) is list, "The input must be a list."
    if len(l)<=1:
        return l
    first=l[0]
    left=[]
    right=[]
    for i in range(1,len(l)):
        if l[i]<first:
            left.append(l[i])
        else:
            right.append(l[i])
    return quick_sort(left)+[first]+quick_sort(right)
