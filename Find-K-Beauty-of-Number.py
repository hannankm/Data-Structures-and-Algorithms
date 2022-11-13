class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        start=count=0
        for end in range(len(num)):
            while end-start==k-1:
                n=num[start:end+1]
                if int(n)!=0 and int(num)%int(n)==0:
                    print(n)
                    count+=1
                start+=1
        return count

        
