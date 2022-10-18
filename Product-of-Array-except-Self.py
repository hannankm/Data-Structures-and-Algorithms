class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*len(nums)
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        for i in range(len(nums)):
            if i==1:
                prefix[i]=nums[i]
            prefix[i]=nums[i]*prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=nums[i]
            else:
                postfix[i]=nums[i]*postfix[i+1]
        for i in range(len(nums)):
            if i==0:
                answer[i]=postfix[i+1]*1
            elif i==len(nums)-1:
                answer[i]=1*prefix[i-1]
            else:
                answer[i]=postfix[i+1]*prefix[i-1]
        return answer 
