class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPair= 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i< j:
                    goodPair+=1
        return goodPair
