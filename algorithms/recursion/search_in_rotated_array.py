"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""


def search_rotated_array(nums: list[int], target: int) -> int:

    def search_helper(nums,target):
        print("new function call")
        len_nums=len(nums)

        if len_nums==0:
            return -1

        if len_nums==1:
            if nums[0]==target: 
                return 0
            else:
                return -1
        
        mid_index=int(len_nums/2)
        
        mid_val=nums[mid_index]
        end_val=nums[len_nums-1]

        if mid_val==target:
            return mid_index
        elif mid_val<target:
            if mid_val<=end_val: # k > mid_index or no rotation
                if target<=end_val: 
                    index=search_helper(nums[mid_index:],target)
                    if index==-1:
                        return -1
                    return mid_index + index
                else: 
                    index=search_helper(nums[:mid_index],target)
                    if index==-1:
                        return -1
                    return index
            else: # mid_val>end_val, i.e. k <= mid_index
                index=search_helper(nums[(mid_index+1):],target)
                if index==-1:
                    return -1
                return mid_index + 1 + index
        else: # mid_val>target:
            if mid_val<=end_val: # k > mid_index or no rotation
                index=search_helper(nums[:mid_index],target)
                if index==-1:
                    return -1
                return index
            else:
                if target<=end_val:
                    index=search_helper(nums[mid_index:],target)
                    if index==-1:
                        return -1
                    return mid_index + index
                else:
                    index=search_helper(nums[:mid_index],target)
                    if index==-1:
                        return -1
                    return index

    return search_helper(nums,target)