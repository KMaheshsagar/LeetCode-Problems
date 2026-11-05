class Solution:
    def climbStairs(self, n: int) -> int:
        def calculate(n,dp):
            if n<0:
                return 0
            if n==0:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]=calculate(n-1,dp)+calculate(n-2,dp)
            return dp[n]
        dp=[-1]*(n+1)
        return calculate(n,dp)