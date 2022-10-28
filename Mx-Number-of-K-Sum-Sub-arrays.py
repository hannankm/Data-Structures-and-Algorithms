class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start=operation=0
        end=len(nums)-1
        while start<end :
            if nums[start]+ nums[end]==k:
                #increment operation
                operation+=1
               #increment start and end pointers
                start+=1
                end-=1
            elif nums[start]+nums[end]>k:
                 #increment end pointer
                end-=1
            else:
                #increment start pointer
                start+=1    
        return operation
