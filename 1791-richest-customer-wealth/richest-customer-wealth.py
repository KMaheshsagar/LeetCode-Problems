class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for i in accounts:
            cursum=sum(i)
            maxwealth=max(cursum,maxwealth)
        return maxwealth
        