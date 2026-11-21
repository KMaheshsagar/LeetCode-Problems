class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for j in range(n - m + 1):
            if haystack[j : j + m] == needle:
                return j
                
        return -1
