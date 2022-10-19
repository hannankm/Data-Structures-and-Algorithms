class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        start, end=0, 0
        length=0
        while end<len(s):            
            while start<end and s[end] in chars:
                chars.remove(s[start])
                start+=1   
            chars.add(s[end])
            end+=1
            length=max(length, end-start)
        return length
