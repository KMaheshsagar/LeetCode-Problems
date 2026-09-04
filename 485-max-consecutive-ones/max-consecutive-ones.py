class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        l=0
        for  r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            else:
                maxi=max(maxi,r-l+1)
        return maxi
                
            



