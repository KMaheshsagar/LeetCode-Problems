class Solution:
    def reverseDegree(self, s: str) -> int:
        totalsum=0
        for i,char in enumerate(s,1):
            reverse_alpha=26-(ord(char)-ord('a'))
            totalsum+=i*reverse_alpha
        return totalsum

        