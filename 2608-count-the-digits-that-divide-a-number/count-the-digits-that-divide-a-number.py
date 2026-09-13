class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        div=num
        while num>0:
            val=num%10
            if div%val==0:
                c+=1
            num=num//10
        return c
        