class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices=[]
        for i in range(len(nums)):
            min=i
            for j in range(i+1, len(nums)):
                if nums[min]>nums[j]:
                    min=j
            nums[min], nums[i]=nums[i], nums[min]
        x=0
        while x<len(nums) and nums[x]<=target:
            if nums[x]==target:
                indices.append(x)
            x+=1
        return indices
                    
