class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        maxlen=0
        for right in range(len(s)):
            if s[right] in seen:
                left=max(left,seen[s[right]]+1)
            seen[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen

