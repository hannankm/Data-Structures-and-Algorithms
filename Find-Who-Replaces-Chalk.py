class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = 0
        for i in chalk: 
            prefix += i
        k = k - (k//prefix * prefix)
        for j, i in enumerate(chalk):
            if i > k: return j
            k -= i
