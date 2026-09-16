class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        prod=1
        while n>0:
            c=n%10
            sums+=c
            prod*=c
            n=n//10
        return prod-sums
