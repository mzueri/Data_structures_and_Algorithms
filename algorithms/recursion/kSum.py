
# Given an array nums of n integers, integer k and a target value, 
# return an array of all the unique k-tuplets [nums[a_1], nums[a_2], ... , nums[a_k]] such that they add up
# to the target value. 
# The output must not contain duplicates (e.g. [1,-1,0] is the same as [-1,1,0]).


# The following algorithm finds a solution in O(n^(k-1)) time (n=len(nums)). 
def kSum(k: int, nums: list[int], target: int) -> list[list[int]]:
        
        # the following assumes that the input nums is sorted and returns all unique 2-combinations which add up to target.
        # This can be done in linear time using a hash map.  
        def twoSum_sorted(sorted_nums, target=0):
            len_nums=len(sorted_nums)
            hash={}
            res=[]
            i=0
            while i<len_nums:
                if target-sorted_nums[i] in hash:
                    res.append([sorted_nums[hash[target-sorted_nums[i]]],sorted_nums[i]])
                    # while loop to go to the next different element (to avoid duplicates).
                    while i+1<len_nums and sorted_nums[i+1]==sorted_nums[i]:
                        i+=1 
                hash[sorted_nums[i]]=i        
                i+=1
            return res

        # the following assumes that the input nums is sorted and returns all unique k-combinations which add up to target.
        # we use recursion to get to the base case when k=2. 
        # Then we use the above function for 2-combs.
        def kSum_sorted(k,sorted_nums,target=0):
            if k==2:
                return twoSum_sorted(sorted_nums,target)
            len_nums=len(sorted_nums)
            res=[]
            i=0
            while i<len_nums:
                k_less_1_combs=kSum_sorted(k-1,sorted_nums[i+1:],target-sorted_nums[i])
                if k_less_1_combs!=[]:
                    res+=[[sorted_nums[i]]+k_less_1_comb for k_less_1_comb in k_less_1_combs]
                # go the next index which has not been considered yet to avoid duplicates.
                while i+1<len_nums and sorted_nums[i+1]==sorted_nums[i]:
                    i+=1
                i+=1
            return res

        # We first sort the array. 
        # This is does not affect the running time efficiency (at least if k>2).
        # Then we can use the above kSum_sorted algorithm.
        return kSum_sorted(k,sorted(nums),target)

#print(kSum(4,[1,0,-1,0,-2,2],0))
#print(kSum(3,[2,2,2,2,2],6))
