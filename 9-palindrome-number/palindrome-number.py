class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=0
        if x<0 or (x%10==0 and x!=0):
            return False
        while(x>c):
            c=c*10+x%10
            x=x//10
        if x==c or x==c//10:
            return True
        return False
            
        