class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisiblesum=0
        non_divisiblesum=0
        for i in range(1,n+1):
            if i%m==0:
                divisiblesum+=i
            else:
                non_divisiblesum+=i
        return non_divisiblesum-divisiblesum
        