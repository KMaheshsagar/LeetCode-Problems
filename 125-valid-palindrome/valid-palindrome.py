class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=[char for char in s if char.isalnum()]
        if l==l[::-1] :
            return True
        return False