class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        result=[0]*2
        while start<end:
            if numbers[start]+ numbers[end]==target:
                result[0], result[1]=start+1, end+1
                return result
            elif numbers[start]+ numbers[end]> target:
                end-=1
            else:
                start+=1class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        result=[0]*2
        while start<end:
            if numbers[start]+ numbers[end]==target:
                result[0], result[1]=start+1, end+1
                return result
            elif numbers[start]+ numbers[end]> target:
                end-=1
            else:
                start+=1
