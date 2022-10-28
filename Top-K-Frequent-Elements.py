class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1
        result = sorted(mapping,key=lambda x:mapping[x], reverse=True)
        return result[:k]
