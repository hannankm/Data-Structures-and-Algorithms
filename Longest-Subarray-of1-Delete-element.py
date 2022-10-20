class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)==nums.count(1):
            return len(nums)-1
        count=0
        count1=0
        max_count=0
        for i in range(len(nums)-1):
            if nums[i]!=0:
                count+=1
            else:
                for j in range(i+1, len(nums)):
                    if nums[j]!=0:
                        count1+=1
                    else:
                        break
                if max_count<count+ count1:
                    max_count=count+ count1
                count=0
                count1=0
        return max_count
                
        
