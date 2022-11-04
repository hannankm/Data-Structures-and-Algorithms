class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        mini=len(nums)+1
        sum=0
        for end in range(len(nums)):
            sum+=nums[end]
            while sum>=target and start<=len(nums):
                mini=min(mini, end-start +1)
                sum-=nums[start]
                start+=1
        if mini== len(nums)+1:
            return 0
        return mini
