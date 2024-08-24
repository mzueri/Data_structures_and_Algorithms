# Algorithm SELECT.
# Given a input list of distinct (can be generalized to arbitrary) integers. 
# Find the k-th smallest element. 
# This algorithm runs in linear time.

import math
from sorting.merge_sort import merge_sort

def SELECT(input_list, k):
    assert isinstance(input_list, list),"Provide the integers in a list."
    assert len(list(set(input_list)))==len(input_list),"TODO: generalize to arbitrary elements. For now, provide distinct integers."
    assert k>=1 and k<=len(input_list),"k must be a positive integer smaller than the length of the input list."

    if len(input_list)<=5:
        sorted_list=merge_sort(input_list)
        return sorted_list[k-1]
    
    len_input_list=len(input_list)
    buckets=[]
    n_buckets=math.ceil(len_input_list/5)
    for i in range(n_buckets):
        if 5*(i+1)<=len_input_list:
            buckets.append(input_list[5*i:5*(i+1)])
        elif 5*i<len_input_list:
            buckets.append(input_list[5*i:])
    #print(buckets)

    bucket_medians=[]
    for bucket in buckets:
        bucket_medians.append(SELECT(bucket,max(1,len(bucket)//2))) 
    median_of_medians=SELECT(bucket_medians,max(1,len(bucket_medians)//2))

    smaller=[]
    larger=[]
    for s in input_list:
        if s<median_of_medians:
            smaller.append(s)
        elif s>median_of_medians:
            larger.append(s)
    
    size_smaller=len(smaller)
    if size_smaller==k-1:
        return median_of_medians
    elif size_smaller>=k:
        return SELECT(smaller,k)
    else:
        return SELECT(larger,k-1-size_smaller)


# test
#import random
#random.seed(10)
#l=list(range(1,1000))
#random.shuffle(l)
#print(SELECT(l,102))
