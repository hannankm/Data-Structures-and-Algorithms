class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        # Iterate all the index up to n also one more n+1
        start, pos = 0, 0
        for end in range(1,n+1):
            if end == n or chars[start] != chars[end]:
                chars[pos] = chars[start]
                pos += 1
                if end - start > 1:                    
                    str_length = str(end - start)
                    for char in str_length:
                        chars[pos] = char
                        pos += 1
                start = end
            
        return pos
