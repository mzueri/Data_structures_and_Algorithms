import math
from typing import Tuple

def is_sorted(input_list:list)->bool:
    assert isinstance(input_list, list),TypeError
    length_input_list=len(input_list)
    if length_input_list<=1:
        return True
    for index in range(length_input_list-1):
        if input_list[index]>input_list[index+1]:
            return False
    return True

def merge(list1:list,list2:list)->list:
    assert isinstance(list1,list) & isinstance(list2,list),TypeError
    sorted_list=[]
    i=0;j=0
    while (i<len(list1)) or (j<len(list2)):
        if i==len(list1):
            sorted_list.append(list2[j])
            j+=1
        elif j==len(list2):
            sorted_list.append(list1[i])
            i+=1
        elif list1[i]<=list2[j]:
            sorted_list.append(list1[i])
            i+=1
        else:
            sorted_list.append(list2[j])
            j+=1
    return sorted_list

def divide(input_list:list)-> Tuple[list,list]:
    assert isinstance(input_list,list),TypeError
    len_input_list=len(input_list)
    mid=math.floor(len_input_list/2)
    return input_list[0:mid],input_list[mid:len_input_list]

def merge_sort(input_list:list)->list:
    assert isinstance(input_list,list),TypeError
    if len(input_list)==1:
        return input_list
    left_half,right_half=divide(input_list)
    return merge(merge_sort(left_half),merge_sort(right_half))