import random
from merge_sort import merge_sort
from quick_sort import quick_sort

random.seed(10)

l=list(range(100000))
l_permutation=l.copy()
random.shuffle(l_permutation)
#print(l_permutation)
#print(l)
results=[merge_sort(l_permutation),
         quick_sort(l_permutation)]      
equality_test=[result==l for result in results]        
print(equality_test)
