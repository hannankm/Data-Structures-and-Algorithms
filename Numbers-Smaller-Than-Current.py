class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        i=0
        while i<len(nums):
            counter=0
            for j in range(len(nums)):
                if nums[i]!= nums[j] and nums[i]>nums[j]:
                    counter+=1
            answer.append(counter)
            i+=1
        return answer
