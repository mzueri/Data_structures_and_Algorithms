# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray(nums):
        
    # Kadane's Algorithm
    
    res=float('-inf')
    curr_sum=0

    for i in range(len(nums)):
        curr_sum+=nums[i] 
        if curr_sum>res:
            res=curr_sum
        if curr_sum<0:
            curr_sum=0 
    
    return res

assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6, "Test case failed. Fix your algorithm."