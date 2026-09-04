class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        l=0
        c=0
        maxiv=0
        for r in range(len(s)):
            if s[r] in vowels:
                c+=1
            if (r-l+1)==k:
                maxiv=max(maxiv,c)
                if s[l] in vowels:
                    c-=1
                l+=1
        return maxiv