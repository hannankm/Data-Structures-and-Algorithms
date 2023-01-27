class Solution(object):
    def isPowerOfThree(self, n):
        if (n <= 0):
            return False
        if (n % 3 == 0):
            return self.isPowerOfThree(n // 3)
        if (n == 1):
            return True
        return False
