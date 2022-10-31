class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        beg=end=0
        num=0
        target=threshold*k
        avg=sum(arr[:k])
        if avg>=target:
            num=1
        for end in range(len(arr)-k):
            avg= avg- arr[end]+arr[end+k]
            if avg>=target:
                num+=1
        return num
