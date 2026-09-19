class Solution:
    def digitsum(self,n):
        if n==0:
            return 0
        return n%10+self.digitsum(n//10)
    def differenceOfSum(self, nums: list[int]) -> int:
        elementsum=sum(nums)
        dsums=0
        for i in nums:
            dsums+=self.digitsum(i)
        return elementsum-dsums

        